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


@dataclass
class User:
    full_name: str
    email: str
    username: str


# business logicul tau- cea mai complexa parte din codul tau
# cerinte de la stakeholderi
class NotificationService:
    def __init__(self, email_sender: EmailSender, userApiAdapter: LdapUserApiClientAdapter):
        self.email_sender = email_sender
        self.userApiAdapter = userApiAdapter

    # aici in zona de business rules ar trebui sa fie codul CEL MAI CURAT
    def send_welcome_email(self, customer: Customer, username_part: str):
        user = userApiAdapter.fetch_user(username_part)

        can_return_orders = customer.gold_member or not customer.legal_entity_code

        email = Email(
            from_addr="noreply@cleanapp.com",
            to=customer.email,
            subject="Welcome!",
            body=(
                f"Welcome {customer.name}!\n"
                f"Remember: you {'can' if can_return_orders else 'cannot'} return orders.\n"
                f"Sincerely,\n{user.full_name}"
            )
        )

        if user.email:
            contact = f"{user.full_name} <{user.email.lower()}>"
            email.cc.append(contact)

        self.email_sender.send_email(email)

        customer.created_by_username = user.username


# class Controller:#
class LdapUserApiClientAdapter:  # Adapter Pattern ®️
    def fetch_user(self, username_part: str) -> User:
        # external 💩
        # retries, authorization, error handling, monitoring their call time
        dto_list = self.ldap_api.search_using_get(username_part.upper(), None, None)
        if len(dto_list) != 1:
            raise ValueError(
                f"Search for username='{username_part}' did not return a single result: {dto_list}"
            )
        ldap_user_dto = dto_list[0]

        return self.map_from_their_dto_to_my_object(ldap_user_dto)

    def map_from_their_dto_to_my_object(self, ldap_user_dto) -> User:
        full_name = f"{ldap_user_dto.fname} {ldap_user_dto.lname.upper()}"
        self.normalize(ldap_user_dto)

        return User(full_name, ldap_user_dto.work_email, ldap_user_dto.un)

    def normalize(self, ldap_user_dto: LdapUserDto):
        if ldap_user_dto.un.startswith("s"):
            ldap_user_dto.un = "system"


# Exemplu de rulare
if __name__ == "__main__":
    service = NotificationService(EmailSender(), LdapApi())
    customer = Customer(name="Victor", email="victor@cleanapp.com", gold_member=True, legal_entity_code="")
    service.send_welcome_email(customer, "john")
