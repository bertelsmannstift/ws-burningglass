# import type hints
from __future__ import annotations

from uuid import uuid4

# import dependencies
from sqlalchemy import (CHAR, BigInteger, Boolean, Column, Date, Enum,
                        ForeignKey, Integer, String, Table)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import foreign, relationship, remote, validates

from models.base_class import Base

textkernel_posting_skills = Table(
    "textkernel_posting_skills",
    Base.metadata,
    Column(
        "posting_id",
        UUID,
        ForeignKey("textkernel_postings.id", ondelete="CASCADE"),
        primary_key=True,
    ),
    Column(
        "skill_id",
        CHAR(length=20),
        ForeignKey("textkernel_skills.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class TextkernelRegion(Base):
    # define table name
    __tablename__ = "textkernel_regions"

    # define fields
    id = Column(CHAR(length=2), primary_key=True)
    label = Column(String(length=126))


class TextkernelSourceType(Base):
    # define table name
    __tablename__ = "textkernel_source_types"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=126))


class TextkernelEducationLevel(Base):
    # define table name
    __tablename__ = "textkernel_education_level"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=126))


class TextkernelContractType(Base):
    # define table name
    __tablename__ = "textkernel_contract_types"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=126))


class TextkernelWorkingHoursType(Base):
    # define table name
    __tablename__ = "textkernel_working_hours_types"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=126))


class TextkernelEmploymentType(Base):
    # define table name
    __tablename__ = "textkernel_employment_types"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=126))


class TextkernelAdvertiserType(Base):
    # define table name
    __tablename__ = "textkernel_advertiser_types"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=126))


class KlassifikationWirtschaftszweige(Base):
    # define table name
    __tablename__ = "klassifikation_wirtschaftszweige"

    # define fields
    id = Column(String(length=10), primary_key=True)
    label = Column(String(length=255))


class TextkernelOrganizationSize(Base):
    # define table name
    __tablename__ = "textkernel_organization_sizes"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=255))


class TextkernelOrganizationIndustry(Base):
    # define table name
    __tablename__ = "textkernel_organization_industries"

    # define fields
    id = Column(Integer, primary_key=True)
    label = Column(String(length=255))


class TextkernelOrganization(Base):
    # define table name
    __tablename__ = "textkernel_organizations"

    # define fields
    id = Column(Integer, primary_key=True)
    national_id = Column(String(length=255), nullable=True, default=None)
    name = Column(String(length=255))
    address = Column(String(length=255), nullable=True, default=None)
    street_number = Column(String(length=255), nullable=True, default=None)
    postal_code = Column(String(length=255), nullable=True, default=None)
    location_id = Column(Integer, nullable=True, default=None)
    location_name = Column(String(length=255), nullable=True, default=None)
    website = Column(String(length=255), nullable=True, default=None)
    linkedin_id = Column(String(length=255), nullable=True, default=None)
    size_id = Column(
        Integer, ForeignKey("textkernel_organization_sizes.id"), nullable=True, default=None
    )
    industry_id = Column(
        Integer, ForeignKey("textkernel_organization_industries.id"), nullable=True, default=None
    )
    klassifikation_wirtschaftszweige_id = Column(
        CHAR(length=10),
        ForeignKey("klassifikation_wirtschaftszweige.id"),
        nullable=True,
        default=None,
    )

    size = relationship("TextkernelOrganizationSize", uselist=False, lazy="selectin")
    industry = relationship("TextkernelOrganizationIndustry", uselist=False, lazy="selectin")
    klassifikation_wirtschaftszweige = relationship(
        "KlassifikationWirtschaftszweige", uselist=False, lazy="selectin"
    )


class TextkernelSkill(Base):
    # define table name
    __tablename__ = "textkernel_skills"

    # define fields
    id = Column(CHAR(length=20), primary_key=True)
    label = Column(String(length=255))
    category = Column(
        Enum(
            "SOFT_SKILL", "PROFESSIONAL_SKILL", "LANGUAGE_SKILL", "IT_SKILL", name="skill_type_enum"
        )
    )


class TextkernelPosting(Base):
    # define table name
    __tablename__ = "textkernel_postings"

    # define fields
    id = Column(UUID, primary_key=True, default=uuid4)
    job_id = Column(UUID, nullable=False)
    sequence_number = Column(BigInteger, nullable=False)
    via_intermediary = Column(Boolean, nullable=True, default=None)
    published_at = Column(Date, nullable=False)
    expired_at = Column(Date, nullable=True, default=None)
    aws_file_key = Column(String(length=255), nullable=False)

    job_title = Column(String(length=512), nullable=True, default=None)
    language = Column(CHAR(length=2), nullable=True, default=None)

    onet_profession_id = Column(
        Integer, ForeignKey("onet_professions.id"), nullable=True, default=None
    )
    isco_profession_id = Column(
        CHAR(length=4), ForeignKey("isco_professions.id"), nullable=True, default=None
    )

    source_url = Column(String(length=255), nullable=True, default=None)
    source_website = Column(String(length=255), nullable=False)
    source_type_id = Column(Integer, ForeignKey("textkernel_source_types.id"), nullable=False)

    location_id = Column(Integer, nullable=True, default=None)
    location_name = Column(String(length=255), nullable=True, default=None)
    location_coordinates = Column(String(length=255), nullable=True, default=None)
    region_id = Column(
        CHAR(length=2), ForeignKey("textkernel_regions.id"), nullable=True, default=None
    )

    advertiser_name = Column(String(length=255), nullable=True, default=None)
    advertiser_street = Column(String(length=255), nullable=True, default=None)
    advertiser_postal_code = Column(String(length=10), nullable=True, default=None)
    advertiser_location = Column(String(length=255), nullable=True, default=None)
    advertiser_website = Column(String(length=255), nullable=True, default=None)
    advertiser_reference_number = Column(String(length=255), nullable=True, default=None)
    available_contact_fields = Column(String(length=512), nullable=True, default=None)

    hours_per_week_from = Column(Integer, nullable=True, default=None)
    hours_per_week_to = Column(Integer, nullable=True, default=None)
    salary = Column(Integer, nullable=True, default=None)
    salary_from = Column(Integer, nullable=True, default=None)
    salary_to = Column(Integer, nullable=True, default=None)
    experience_years_from = Column(Integer, nullable=True, default=None)
    experience_years_to = Column(Integer, nullable=True, default=None)

    education_level_id = Column(
        Integer, ForeignKey("textkernel_education_level.id"), nullable=True, default=None
    )
    contract_type_id = Column(
        Integer, ForeignKey("textkernel_contract_types.id"), nullable=True, default=None
    )
    working_hours_type_id = Column(
        Integer, ForeignKey("textkernel_working_hours_types.id"), nullable=True, default=None
    )
    employment_type_id = Column(
        Integer, ForeignKey("textkernel_employment_types.id"), nullable=True, default=None
    )
    advertiser_type_id = Column(
        Integer, ForeignKey("textkernel_advertiser_types.id"), nullable=True, default=None
    )
    organization_id = Column(
        Integer, ForeignKey("textkernel_organizations.id"), nullable=True, default=None
    )

    region = relationship("TextkernelRegion", uselist=False, lazy="selectin")
    education_level = relationship("TextkernelEducationLevel", uselist=False, lazy="selectin")
    contract_type = relationship("TextkernelContractType", uselist=False, lazy="selectin")
    working_hours_type = relationship("TextkernelWorkingHoursType", uselist=False, lazy="selectin")
    employment_type = relationship("TextkernelEmploymentType", uselist=False, lazy="selectin")
    isco_profession = relationship("IscoProfession", uselist=False, lazy="selectin")
    onet_profession = relationship("OnetProfession", uselist=False, lazy="selectin")
    source_type = relationship("TextkernelSourceType", uselist=False, lazy="selectin")
    advertiser_type = relationship("TextkernelAdvertiserType", uselist=False, lazy="selectin")
    organization = relationship("TextkernelOrganization", uselist=False, lazy="selectin")

    def to_dict(self):
        return dict([(k, getattr(self, k)) for k in self.__dict__.keys() if not k.startswith("_")])

    @validates(
        "job_title",
        "source_url",
        "source_website",
        "advertiser_name",
        "advertiser_street",
        "advertiser_postal_code",
        "advertiser_location",
        "advertiser_website",
        "advertiser_reference_number",
        "available_contact_fields",
        "location_name",
    )
    def validate_code(self, key, value):
        max_len = getattr(self.__class__, key).prop.columns[0].type.length
        if value and len(value) > max_len:
            return value[:max_len]
        return value
