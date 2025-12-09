def main():
    while True:
        try:
            # Prompt user for fraction
            prompt = input("Fraction: ")
            # Split string on division
            num_list = prompt.split("/")
            # Convert numerator & denomeator into int and div to get decimal
            decimal = int(num_list[0])/int(num_list[1])
            # Multiply decimal by 100 and add % to form percent
            percent = str(int(decimal*100))+"%"
            if int(num_list[0]) < 0 or int(num_list[0]) > int(num_list[1]):
                raise ValueError
        except ValueError:
            # If ValueError, reprompt for Fraction
            pass
        except ZeroDivisionError:
            # If ZeroDivisionError, reprompt for fraction
            pass
        else:
            # If 100%, return "F"
            if percent == "100%":
                print("F")
            # If 0%, return "E"
            elif percent == "0%":
                print("E")
            # Other percentages, return
            else:
                print(percent)
            break

main()
