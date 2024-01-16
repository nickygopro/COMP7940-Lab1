def print_factor(x):
        result = []
        for i in range(1, x+1):
                if x%i == 0 and i != 0:
                        result.append(i)
        return result

def main():
        l = [52633, 8137, 1024, 999]
        for item in l:
                print(print_factor(item))


if __name__ == '__main__':
	main()
