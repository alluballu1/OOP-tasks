class cookie:

    def __init__(self, init_shape, init_flavor):
        self.__shape = init_shape
        self.__flavor = init_flavor


    def set_shape(self, desired_shape):
        self.__shape = desired_shape


    def get_shape(self):
        return  self.__shape

    def set_flavor(self, desired_flavor):
        self.__flavor = desired_flavor

    def __str__(self):
        return "Your cookie is " + self.__shape + "-shaped and tastes like " + format(self.__flavor)
