from dataclasses import dataclass, field


@dataclass(order=True, frozen=True)
class Customer:
    sort_index: int = field(init=False, repr=False)
    id_number: int
    name: str

    def __post_init__(self):
        # self.sort_index = self.id_number
        object.__setattr__(self, "sort_index", self.id_number)


if __name__ == "__main__":
    customer_ms = Customer(2, "Mary Smith")
    customer_jd = Customer(1, "John Doe")
    duplicate_of_customer_jd = Customer(1, "John Doe")

    print(id(customer_jd))
    print(id(duplicate_of_customer_jd))
    print(customer_jd == duplicate_of_customer_jd)  # True

    print(customer_ms > customer_jd)  # True

    customer_ms.id_number = 17  # raises a `dataclasses.FrozenInstanceError`
