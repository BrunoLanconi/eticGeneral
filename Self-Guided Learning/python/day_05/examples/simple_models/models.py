from pydantic import BaseModel  # type: ignore


class MyModel(BaseModel):
    """
    MyModel class represents a model with mandatory, default, and optional attributes.

    Attributes:
        mandatoryAttribute (str): The mandatory attribute of the model.
        defaultAttribute (str, optional): The default attribute of the model. Defaults to "Default Value".
        optionalAttribute (str or None, optional): The optional attribute of the model. Defaults to None.
    """

    mandatoryAttribute: str
    defaultAttribute: str = "Default Value"
    optionalAttribute: str | None = None
