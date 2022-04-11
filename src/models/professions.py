# import dependencies
from sqlalchemy import CHAR, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from models.base_class import Base


class OnetProfessionClass(Base):
    # define table name
    __tablename__ = "onet_profession_classes"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=512), nullable=False)


class OnetProfessionGroup(Base):
    # define table name
    __tablename__ = "onet_profession_groups"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=512), nullable=False)
    onet_profession_class_id = Column(Integer, ForeignKey("onet_profession_classes.id"))


class OnetProfession(Base):
    # define table name
    __tablename__ = "onet_professions"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=512), nullable=False)
    onet_profession_group_id = Column(Integer, ForeignKey("onet_profession_groups.id"))


class IscoProfessionMajor(Base):
    # define table name
    __tablename__ = "isco_profession_major"

    # define fields
    id = Column(CHAR(length=1), primary_key=True)
    en = Column(String(length=255), nullable=False)
    de = Column(String(length=255), nullable=False)

    children = relationship("IscoProfessionSubMajor", lazy="subquery")


class IscoProfessionSubMajor(Base):
    # define table name
    __tablename__ = "isco_profession_sub_major"

    # define fields
    id = Column(CHAR(length=2), primary_key=True)
    en = Column(String(length=255), nullable=False)
    de = Column(String(length=255), nullable=False)
    isco_profession_major_id = Column(CHAR(length=1), ForeignKey("isco_profession_major.id"))

    children = relationship("IscoProfessionMinor", lazy="subquery")


class IscoProfessionMinor(Base):
    # define table name
    __tablename__ = "isco_profession_minor"

    # define fields
    id = Column(CHAR(length=3), primary_key=True)
    en = Column(String(length=255), nullable=False)
    de = Column(String(length=255), nullable=False)
    isco_profession_sub_major_id = Column(
        CHAR(length=2), ForeignKey("isco_profession_sub_major.id")
    )

    children = relationship("IscoProfession", lazy="subquery")


class IscoProfession(Base):
    # define table name
    __tablename__ = "isco_professions"

    # define fields
    id = Column(CHAR(length=4), primary_key=True)
    en = Column(String(length=255), nullable=False)
    de = Column(String(length=255), nullable=False)
    isco_profession_minor_id = Column(CHAR(length=3), ForeignKey("isco_profession_minor.id"))
