from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Literal, Annotated, Optional

class responsemodel(BaseModel):
    response:Annotated[Literal["Low","High","Medium"],Field(...,description="category")]
    #response_confidence:Annotated[float,Field(...,description="confidence of the selected category")]
    all_class_probs:Annotated[dict[str,float],Field(...,description="all class probabilities")]