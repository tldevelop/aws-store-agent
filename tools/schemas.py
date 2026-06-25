from typing import Self
from pydantic import BaseModel, Field, PositiveFloat, NonNegativeInt, model_validator

class ProductName(BaseModel):
    product_name:str = Field(
        ...,
        description='The name of the product'
    )

class ProductData(BaseModel):
    price:PositiveFloat = Field(
        ...,
        description='The price amount of the product'
    )
    quantity:NonNegativeInt = Field(
        ...,
        description='The quantity of the product'
    )
    description:str = Field(
        ...,
        description='The description/details of the product'
    )

class CreateToolSchema(ProductName, ProductData):
    pass

class UpdateToolSchema(ProductName):
    price:PositiveFloat | None = Field(
        None,
        description='The price amount of the product'
    )
    quantity:NonNegativeInt | None = Field(
        None,
        description='The quantity of the product'
    )
    description:str | None = Field(
        None,
        description='The description/details of the product'
    )

    @model_validator(mode="after")
    def non_empty_update(self) -> Self:
        update_fields = self.model_dump(
            exclude={"product_name"},
            exclude_none=True,
        )
        if not update_fields:
            raise ValueError("At least one field must be provided to update the product")
        return self

class DeleteToolSchema(ProductName):
    pass