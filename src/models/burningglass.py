# import type hints
from __future__ import annotations

from uuid import uuid4

# import dependencies
from sqlalchemy import (CHAR, VARCHAR, BigInteger, Boolean, Column, Date, Enum,
                        ForeignKey, Integer, String, Table)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import foreign, relationship, remote, validates

from models.base import Base


class BurningGlassBase(Base):
    __table_args__ = {"schema": "burningglass"}


class BurningGlassCategorySector(BurningGlassBase):
    # define table name
    __tablename__ = "l_category_sector"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassContract(BurningGlassBase):
    # define table name
    __tablename__ = "l_contract"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassCountry(BurningGlassBase):
    # define table name
    __tablename__ = "l_country"

    # define fields
    id = Column(VARCHAR(length=2), primary_key=True)
    title = Column(String)


class BurningGlassEducationalLevel(BurningGlassBase):
    # define table name
    __tablename__ = "l_educational_level"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassEscoLevel1(BurningGlassBase):
    # define table name
    __tablename__ = "l_esco_level_1"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassEscoLevel2(BurningGlassBase):
    # define table name
    __tablename__ = "l_esco_level_2"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassEscoLevel3(BurningGlassBase):
    # define table name
    __tablename__ = "l_esco_level_3"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassEscoLevel4(BurningGlassBase):
    # define table name
    __tablename__ = "l_esco_level_4"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassEscoSkillLevel3(BurningGlassBase):
    # define table name
    __tablename__ = "l_escoskill_level_3"

    # define fields
    id = Column(BigInteger, primary_key=True)
    title = Column(String)


class BurningGlassExperience(BurningGlassBase):
    # define table name
    __tablename__ = "l_experience"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassMacroRegion(BurningGlassBase):
    # define table name
    __tablename__ = "l_macro_region"

    # define fields
    id = Column(CHAR(length=3), primary_key=True)
    title = Column(String)


class BurningGlassMacroSector(BurningGlassBase):
    # define table name
    __tablename__ = "l_macro_sector"

    # define fields
    id = Column(CHAR(length=1), primary_key=True)
    title = Column(String)


class BurningGlassProvince(BurningGlassBase):
    # define table name
    __tablename__ = "l_province"

    # define fields
    id = Column(CHAR(length=5), primary_key=True)
    title = Column(String)


class BurningGlassRegion(BurningGlassBase):
    # define table name
    __tablename__ = "l_region"

    # define fields
    id = Column(CHAR(length=4), primary_key=True)
    title = Column(String)


class BurningGlassSalary(BurningGlassBase):
    # define table name
    __tablename__ = "l_salary"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassSector(BurningGlassBase):
    # define table name
    __tablename__ = "l_sector"

    # define fields
    id = Column(VARCHAR(length=2), primary_key=True)
    title = Column(String)


class BurningGlassWorkingHour(BurningGlassBase):
    # define table name
    __tablename__ = "l_working_hours"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassPosting(BurningGlassBase):
    # define table name
    __tablename__ = "f_postings"

    # define fields
    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, primary_key=True)
    year_grab_date = Column(Integer)
    month_grab_date = Column(Integer)
    day_grab_date = Column(Integer)
    year_expire_date = Column(Integer)
    month_expire_date = Column(Integer)
    day_expire_date = Column(Integer)
    idesco_level_1 = Column(Integer)
    idesco_level_2 = Column(Integer)
    idesco_level_3 = Column(Integer)
    idesco_level_4 = Column(Integer)
    idprovince = Column(VARCHAR(length=5))
    idregion = Column(VARCHAR(length=4))
    idmacro_region = Column(VARCHAR(length=3))
    idcountry = Column(VARCHAR(length=2))
    idcontract = Column(Integer)
    idsector = Column(Integer)
    idmacro_sector = Column(VARCHAR(length=1))
    idcategory_sector = Column(Integer)
    idsalary = Column(Integer)
    idworking_hours = Column(Integer)
    idexperience = Column(Integer)
    source_category = Column(String)
    sourcecountry = Column(String)
    companyname = Column(String)


class BurningGlassSkill(BurningGlassBase):
    # define table name
    __tablename__ = "f_skills"

    # define fields
    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, primary_key=True)
    escoskill_level_3_id = Column(BigInteger)
