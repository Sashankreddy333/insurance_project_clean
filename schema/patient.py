
from pydantic import BaseModel,Field,computed_field
from typing import Literal, Annotated, Optional
from config.cities import tier_1_cities,tier_2_cities

class patient(BaseModel):
    age:Annotated[int,Field(..., description="age of the patient",gt=0,lt=100)]
    weight:Annotated[float,Field(...,description="patient weight",gt=0)]
    height:Annotated[float,Field(...,description="patient height in m",gt=0)]
    income_lpa:Annotated[float,Field(...,description="income",gt=0)]
    smoker:Annotated[bool,Field(...,description="is Smoker")]
    city:Annotated[str,Field(...,description="city")]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job','business_owner', 'unemployed', 'private_job'],Field(...,description="occupation of the patient")]
    
    @computed_field
    @property
    def bmi(self)->float:
        return round(self.weight/(self.height**2),2)
    @computed_field
    @property
    def agegroup(self)->str:
        if self.age<25:
            return "young"
        elif self.age<45:
            return "adult"
        elif self.age<60:
            return "middleage"
        return "senior"
    @computed_field
    @property
    def lifestylerisk(self)->str:
        if self.smoker and self.bmi>30:
            return "high"
        elif self.smoker and self.bmi>27:
               return "medium"
        else:
            return "low"
    @computed_field
    @property
    def city_tier(self)->int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3