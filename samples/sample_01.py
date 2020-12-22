class Foo():

    def test_1(self):
        self.target.run("abc def")

    def test_2(self):
        a = "abc"
        b = "def"
        self.target.run(a + b)

    def test_3(self):
        a = "abc"
        b = "def"
        self.target.run("{} {}".format(a, b))

    def test_4(self):
        a = "abc"
        b = "def"
        for x in [a, b]:
            self.target.run(x)