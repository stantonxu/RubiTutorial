from rubicon.objc import NSObject, objc_method, objc_property


class Handler(NSObject):
    value = objc_property()

    @objc_method
    def initWithValue_(self, v: int):
        self.value = v
        return self

    @objc_method
    def pokeWithValue_andName_(self, v: int, name) -> float:
        print("My name is ", name)
        return v / 2.0


if __name__ == '__main__':
    my_handler = Handler.alloc().initWithValue(42)
    print(my_handler.value)
    print(my_handler.pokeWithValue(37, andName="Alice"))
