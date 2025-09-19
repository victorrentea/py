from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Customer:
    name: str
    email: str
    gold_member: bool
    legal_entity_code: str
    created_by_username: Optional[str] = None


@dataclass
class Email:
    from_addr: str
    to: str
    subject: str
    body: str
    cc: List[str] = field(default_factory=list)


@dataclass  # din swagger generat de remote API
class LdapUserDto:
    fname: str
    lname: str
    work_email: Optional[str]
    un: str  # username


class EmailSender:
    def send_email(self, email: Email):
        print(f"Sending email to {email.to} with subject '{email.subject}'")


class LdapApi:
    def search_using_get(self, username_upper: str, a, b) -> List[LdapUserDto]:
        # simulare LDAP
        if username_upper == "JOHN":
            return [LdapUserDto("John", "Doe", "john.doe@company.com", "jdoe")]
        return []


class NotificationService:
    def __init__(self, email_sender: EmailSender, ldap_api: LdapApi):
        self.email_sender = email_sender
        self.ldap_api = ldap_api

    def send_welcome_email(self, customer: Customer, username_part: str):
        ldap_user_dto = self.fetch_user_from_ldap(username_part)

        full_name = f"{ldap_user_dto.fname} {ldap_user_dto.lname.upper()}"
        can_return_orders = customer.gold_member or not customer.legal_entity_code

        email = Email(
            from_addr="noreply@cleanapp.com",
            to=customer.email,
            subject="Welcome!",
            body=(
                f"Welcome {customer.name}!\n"
                f"Remember: you {'can' if can_return_orders else 'cannot'} return orders.\n"
                f"Sincerely,\n{full_name}"
            )
        )

        if ldap_user_dto.work_email:
            contact = f"{full_name} <{ldap_user_dto.work_email.lower()}>"
            email.cc.append(contact)

        self.email_sender.send_email(email)

        self.normalize(ldap_user_dto)
        customer.created_by_username = ldap_user_dto.un

    def fetch_user_from_ldap(self, username_part: str) -> LdapUserDto:
        dto_list = self.ldap_api.search_using_get(username_part.upper(), None, None)
        if len(dto_list) != 1:
            raise ValueError(
                f"Search for username='{username_part}' did not return a single result: {dto_list}"
            )
        return dto_list[0]

    def normalize(self, ldap_user_dto: LdapUserDto):
        if ldap_user_dto.un.startswith("s"):
            ldap_user_dto.un = "system"


# Exemplu de rulare
if __name__ == "__main__":
    service = NotificationService(EmailSender(), LdapApi())
    customer = Customer(name="Victor", email="victor@cleanapp.com", gold_member=True, legal_entity_code="")
    service.send_welcome_email(customer, "john")
