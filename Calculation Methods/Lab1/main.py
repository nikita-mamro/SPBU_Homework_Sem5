import logic
import settings


def print_title():
    print("\nЛабораторная 1\n")
    print("Тема:", settings.TOPIC, "\n")
    print("Исходные параметры задачи:")
    print("f(x) = ", settings.F_STRING)
    print("[A, B] = [", settings.A, ",", settings.B, "]")
    print("\u03B5 = ", settings.EPSILON, "\n")


def main():
    print_title()

    print("Процедура отделения корней:")
    sections = logic.root_separation(
        settings.f, 0.00001, settings.A, settings.B)

    print("Метод бисекции")
    logic.bisection_method()

    print("Метод Ньютона")
    logic.newton_method()

    print("Метод Ньютона (модифицированный)")
    logic.modified_newton_method()

    print("Метод секущих")
    logic.secant_method()


if __name__ == "__main__":
    main()
