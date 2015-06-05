def isInvalidInput(string):
    """
    :無効な文字列かどうかのチェック
    :
    :param str string: チェックしたい文字列
    :return bool: 無効な文字列だとTrue
    """

    # 数字で無ければ終了
    if not inputString.isdigit():
        print("Please input a number")
        return True

    # 4桁でなければ終了
    if not len(inputString) == DIGIT_NUMBER:
        print("Please input a 4-digit number")
        return True

    # 重複のない数字のみ許可
    if not len(frozenset(inputString)) == DIGIT_NUMBER:
        print("Please remove duprecate values")
        return True
    return False


def generateTargetNumList(digit):
    """
    :ターゲットとなる番号文字列リストの作製
    :
    :param int digit: 作製したい番号リストの桁数(1~9)
    :return [str, ...]: 重複のないdigit桁数の数字の文字列のリスト
    """

    import random

    selectedNumList = []
    numList = list(range(1, 10))

    for _ in range(digit):
        num = numList.pop(random.randint(0, len(numList) - 1))
        selectedNumList.append(str(num))

    return selectedNumList


def checkHitAndBlowCount(targetNumList, inputNumList):
    """
    :targetNumListの番号文字列リストとinputNumListの番号文字列リストを比較し、
    :数字が含まれ桁が合ってる数(hit)と数字が含まれ桁が合っていない(blow)を計算
    :
    :param [str, ...] targetNumList: 比較したい文字列リスト
    :param [str, ...] inputNumList: 比較したい文字列リスト
    :return (hit, blow): hitとblowの数
    """
    blow = 0
    hit = 0

    for i, e in enumerate(inputNumList):
        if e == targetNumList[i]:
            hit += 1
            continue

        if e in targetNumList:
            blow += 1

    return hit, blow

if __name__ == "__main__":

    DIGIT_NUMBER = 4
    playing = True

    targetNumList = generateTargetNumList(DIGIT_NUMBER)

    print("please input {}-digit number".format(DIGIT_NUMBER))

    while playing:

        # プロンプト
        print(">", end="")

        inputString = input()

        if isInvalidInput(inputString):
            continue

        hit, blow = checkHitAndBlowCount(targetNumList, list(inputString))

        print("{}Hit {}Blow".format(hit, blow))
        if hit == DIGIT_NUMBER:
            playing = False

    print("You win")
