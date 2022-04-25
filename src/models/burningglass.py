# import type hints
from __future__ import annotations

from uuid import uuid4

# import dependencies
from sqlalchemy import (CHAR, VARCHAR, BigInteger, Boolean, Column, Date, Enum,
                        ForeignKey, Integer, String, Table)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import foreign, relationship, remote, validates

from models.base import Base


class BurningGlassCategorySector(Base):
    # define table name
    __tablename__ = "burningglass_l_category_sector"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassContract(Base):
    # define table name
    __tablename__ = "burningglass_l_contract"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassCountry(Base):
    # define table name
    __tablename__ = "burningglass_l_country"

    # define fields
    id = Column(VARCHAR(length=2), primary_key=True)
    title = Column(String)


class BurningGlassEducationalLevel(Base):
    # define table name
    __tablename__ = "burningglass_l_educational_level"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassEscoLevel1(Base):
    # define table name
    __tablename__ = "burningglass_l_esco_level_1"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassEscoLevel2(Base):
    # define table name
    __tablename__ = "burningglass_l_esco_level_2"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassEscoLevel3(Base):
    # define table name
    __tablename__ = "burningglass_l_esco_level_3"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassEscoLevel4(Base):
    # define table name
    __tablename__ = "burningglass_l_esco_level_4"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassEscoSkillLevel3(Base):
    # define table name
    __tablename__ = "burningglass_l_escoskill_level_3"

    # define fields
    id = Column(BigInteger, primary_key=True)
    title = Column(String)


class BurningGlassExperience(Base):
    # define table name
    __tablename__ = "burningglass_l_experience"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassMacroRegion(Base):
    # define table name
    __tablename__ = "burningglass_l_macro_region"

    # define fields
    id = Column(CHAR(length=3), primary_key=True)
    title = Column(String)


class BurningGlassMacroSector(Base):
    # define table name
    __tablename__ = "burningglass_l_macro_sector"

    # define fields
    id = Column(CHAR(length=1), primary_key=True)
    title = Column(String)


class BurningGlassProvince(Base):
    # define table name
    __tablename__ = "burningglass_l_province"

    # define fields
    id = Column(CHAR(length=5), primary_key=True)
    title = Column(String)


class BurningGlassRegion(Base):
    # define table name
    __tablename__ = "burningglass_l_region"

    # define fields
    id = Column(CHAR(length=4), primary_key=True)
    title = Column(String)


class BurningGlassSalary(Base):
    # define table name
    __tablename__ = "burningglass_l_salary"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassSector(Base):
    # define table name
    __tablename__ = "burningglass_l_sector"

    # define fields
    id = Column(VARCHAR(length=2), primary_key=True)
    title = Column(String)


class BurningGlassWorkingHour(Base):
    # define table name
    __tablename__ = "burningglass_l_working_hours"

    # define fields
    id = Column(Integer, primary_key=True)
    title = Column(String)


class BurningGlassPosting(Base):
    # define table name
    __tablename__ = "burningglass_f_postings"

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
    title = Column(String)


class BurningGlassSkill(Base):
    # define table name
    __tablename__ = "burningglass_f_skills"

    # define fields
    id = Column(Integer, primary_key=True)
    general_id = Column(Integer, primary_key=True)
    escoskill_level_3_id = Column(BigInteger)
