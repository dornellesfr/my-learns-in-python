import accounts as acc
import person
import client as cl


class Bank:
    def __init__(
        self,
        name: str,
        agencys: list[int] | None = None,
        clients: list[person.Person] | None = None,
        accounts: list[acc.Account] | None = None,
    ) -> None:
        self.name = name
        self.agencys = agencys or []
        self.clients = clients or []
        self.accounts = accounts or []

    def _agency_check(self, account: acc.Account) -> bool:
        if account.agency in self.agencys:
            return True
        return False

    def _client_check(self, client: cl.Client) -> bool:
        if client in self.clients:
            return True
        return False

    def _acc_check(self, account: acc.Account):
        if account in self.accounts:
            return True
        return False

    def _check_client_acc(self, client: cl.Client, acc: acc.Account):
        if client.account is acc:
            return True
        return False

    def auth(self, client: cl.Client, account: acc.Account):
        validation = self._agency_check(account) \
            and self._client_check(client) \
            and self._acc_check(account) \
            and self._check_client_acc(client, account)

        return validation

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        attr = f'{self.name}, {self.agencys}, {self.accounts}, {self.clients}'
        return f'{class_name}({attr})'


if __name__ == '__main__':
    client1 = cl.Client('Fernando', 22)
    cc1 = acc.CheckingAccount(1589, 1000, 500, 200)
    client1.account = cc1

    c2 = cl.Client('Maria', 66)
    cp1 = acc.CheckingAccount(1212, 2900, 50000)
    c2.account = cp1

    bb = Bank('Banco do Brasil', [1212], [c2], [cp1])
    itau = Bank('Itaú', [1589], [client1], [cc1])

    print(itau.auth(client1, cc1))

    # print(itau)
