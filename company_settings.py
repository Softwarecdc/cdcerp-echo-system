# company_settings.py
# CDCERP Echo System - Company Settings Module

class CompanySettings:
    def __init__(self, company_name, registration_number, vat_number, address, contact_email):
        self.company_name = company_name
        self.registration_number = registration_number
        self.vat_number = vat_number
        self.address = address
        self.contact_email = contact_email

    def __str__(self):
        return (
            f"Company Name: {self.company_name}\n"
            f"Registration Number: {self.registration_number}\n"
            f"VAT Number: {self.vat_number}\n"
            f"Address: {self.address}\n"
            f"Contact Email: {self.contact_email}"
        )

settings = CompanySettings(
    company_name="cdc",
    registration_number="utuytut",
    vat_number="907097",
    address="cape town",
    contact_email="contact@example.com"
)

print(settings)
