from dataclasses import dataclass, field
from typing import List


@dataclass(frozen=True, order=True)
class Customer:
    id_number: int
    name: str
    order_ids: List[int] = field(
        default_factory=list, hash=False, repr=False,
    )
    sort_index: int = field(
        init=False, repr=False,
    )

    def __post_init__(self):
        # self.sort_index = self.id_number
        object.__setattr__(self, "sort_index", self.id_number)


if __name__ == "__main__":
    customer_ms = Customer(2, "Mary Smith", [3, 4])
    customer_jd = Customer(1, "John Doe", [1, 2])
    duplicate_of_customer_jd = Customer(1, "John Doe", [1, 2])

    print(customer_jd)  # Customer(id_number=1, name='John Doe')

    print(id(customer_jd))
    print(id(duplicate_of_customer_jd))
    print(customer_jd == duplicate_of_customer_jd)  # True

    print(customer_ms > customer_jd)  # True

    customer_ms.id_number = 17  # raises a `dataclasses.FrozenInstanceError`
