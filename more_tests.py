import os

def write_file(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content.strip() + "\n")

write_file("tests/test_remedy_plane_objects.py", """
import pytest
from app.remedy_plane.models import RemedyObject, HarmRecord
from app.remedy_plane.enums import RemedyClass, HarmClass

def test_remedy_object_creation():
    remedy = RemedyObject(
        remedy_id="rem-001",
        remedy_class=RemedyClass.CUSTOMER_HARM_REMEDY,
        owner="user",
        scope="global",
        harms=[
            HarmRecord(
                harm_id="harm-1",
                harm_class=HarmClass.CUSTOMER_HARM,
                description="data loss",
                affected_party="customer_A",
                proof_notes="log id 1"
            )
        ]
    )
    assert remedy.remedy_id == "rem-001"
    assert len(remedy.harms) == 1
    assert remedy.harms[0].harm_class == HarmClass.CUSTOMER_HARM
""")

write_file("tests/test_remedy_plane_harms.py", """
import pytest
from app.remedy_plane.models import HarmRecord
from app.remedy_plane.enums import HarmClass

def test_harm_record():
    harm = HarmRecord(
        harm_id="h-001",
        harm_class=HarmClass.FINANCIAL_HARM,
        description="overcharge by 100",
        affected_party="tenant_b",
        proof_notes="invoice 123"
    )
    assert harm.harm_class == HarmClass.FINANCIAL_HARM
    assert harm.is_breach_derived == False
""")
