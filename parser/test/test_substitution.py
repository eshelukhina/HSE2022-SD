from parser.substitution import Substitution


def test_empty_dollar():
    subst = Substitution()
    input_str = "$"
    assert subst.substitute(input_str) == "$"


def test_dollar_and_subst():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    input_str = "$$x"
    assert subst.substitute(input_str) == "$3"


def test_multiple_subst():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    subst.env.add_var(name="y", value="4")
    input_str = "$x$y"
    assert subst.substitute(input_str) == "34"


def test_multiple_subst_with_spaces():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    subst.env.add_var(name="y", value="4")
    subst.env.add_var(name="z", value="7")
    input_str = "$x + $y = $z"
    assert subst.substitute(input_str) == "3 + 4 = 7"


def test_in_single_double_quotes():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    input_str = "\"$x\""
    assert subst.substitute(input_str) == "\"3\""


def test_in_double_double_quotes():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    input_str = "\"\"$x\"\""
    assert subst.substitute(input_str) == "\"\"3\"\""


def test_in_single_single_quotes():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    input_str = "'$x'"
    assert subst.substitute(input_str) == "'$x'"


def test_in_double_single_quotes():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    input_str = "''$x''"
    assert subst.substitute(input_str) == "''3''"


def test_double_in_single_quotes():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    input_str = "'\"$x\"'"
    assert subst.substitute(input_str) == "'\"$x\"'"


def test_single_in_double_quotes():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    input_str = '"\'$x\'"'
    assert subst.substitute(input_str) == '"\'3\'"'


def test_single_and_double():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    input_str = '\'"\'"$x"'
    assert subst.substitute(input_str) == '\'"\'"3"'


def test_multiple_subst_in_double_quotes_1():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    subst.env.add_var(name="y", value="4")
    input_str = '"$x" "$y"'
    assert subst.substitute(input_str) == '"3" "4"'


def test_multiple_subst_in_double_quotes_2():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    subst.env.add_var(name="y", value="4")
    input_str = '"$x $y"'
    assert subst.substitute(input_str) == '"3 4"'


def test_one_single_in_double_quotes_right():
    subst = Substitution()
    input_str = "\" hello' \""
    assert subst.substitute(input_str) == "\" hello' \""


def test_one_single_in_double_quotes():
    subst = Substitution()
    subst.env.add_var(name="x", value="3")
    input_str = "\"'$x\"\""
    assert subst.substitute(input_str) == "\"'3\"\""

