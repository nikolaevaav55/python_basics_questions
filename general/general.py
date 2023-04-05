# list_comprehension

def list_comprehension_1(my_range: int) -> list:
    my_list = [x**2 for x in range(my_range)]
    return my_list


def list_comprehension_2(my_list: list) -> list:
    new_list = [x for x in my_list if "a" in x]
    return new_list

# decorators
def benchmark_simple(funk):
    import time

    def wrapper():
        start = time.time()
        funk()
        end = time.time()
        print(f"Время выполнения: {end-start} секунд")
    return wrapper

@benchmark_simple

def fetch_webpage():
    import requests
    webpage = requests.get("https://google.com")

# decorators with arguments
def benchmark_arguments(iters):
    def actual_decorator(func):
        import time

        def wrapper(*args, **kwargs):
            total = 0
            for i in range(iters):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end - start)
            print(f"Среднее время выполнения: {end-start} секунд")
            return return_value
        return wrapper
    return actual_decorator

@benchmark_arguments(iters = 10)
def fetch_webpage_2(url):
    import requests
    webpage = requests.get(url)
    return webpage.text


if __name__ == '__main__':
    print(list_comprehension_1(10))
    print(list_comprehension_2(['kiwi', 'mango', 'apple']))
    fetch_webpage()

    webpage = fetch_webpage_2('http://google.com')
    print(webpage)