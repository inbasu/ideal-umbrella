import sys


class ArgsError(Exception):
    pass


class Token:
    pass


class Scanner:
    def scane_tokens(self, line: str) -> list[Token]:
        return []


class ErrorReporter:
    pass


class Lox:

    had_error = False
    scanner = Scanner()

    def main(self, args: list[str]) -> None:
        if len(args) > 1:
            raise ArgsError
        elif len(args) == 1:
            self.run_file(args[0])
        else:
            self.run_promt()

    def run(self, line_of_code: str) -> None:
        tokens: list[Token] = self.scanner.scane_tokens(line_of_code)

        # temp
        for token in tokens:
            print(token)

    def error(self, line: int, message: str) -> None:
        self.report(line, "", message)

    def report(self, line: int, where: str, message: str) -> None:
        print(f"[line {line}] Error {where}: {message}")
        self.had_error = True

    def run_file(self, file: str):
        raise NotImplementedError

    def run_promt(self):
        while True:
            self.had_error = False
            line = input(">>")
            if not line:
                break
            self.run(line)


if __name__ == "__main__":
    Lox().main(sys.argv[1:])
