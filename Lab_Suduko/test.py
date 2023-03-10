import CSProblem


def squreTest():
    assert CSProblem.first_spot_in_box(8) == CSProblem.first_spot_in_box(25)
    assert CSProblem.first_spot_in_box(20) == CSProblem.first_spot_in_box(11)
    assert CSProblem.first_spot_in_box(50) == CSProblem.first_spot_in_box(41)
    assert CSProblem.first_spot_in_box(80) == CSProblem.first_spot_in_box(71)
    assert CSProblem.first_spot_in_box(72) == CSProblem.first_spot_in_box(74)
    assert CSProblem.first_spot_in_box(47) == CSProblem.first_spot_in_box(36)

if __name__=="__main__":
    squreTest()
