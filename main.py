"""
God Melody
          by l2G7
              """
# main.py

# Импорт модулей
import random
from rich.console import Console

# для rich
console = Console()

# Для преобразования в HEX
def to_hex(number: int, length: int = 2):
    # Этот код сделала нейросеть потому что прошлый был по её словам "говно полное", но всё остальное чисто делал я.
    hex_number: str = hex(number)[2:].upper()
    return_number = hex_number.zfill(length)
    return return_number

# Эта функция просит бога создать команду и возвращает её.
def get_command():
    command: str = ""
    command_operand2, command_operand3, command_operand4 = None, None, None
    command_operation_id = random.randint(0,15)

    if command_operation_id == 0:
        # defBuzPin=
        command_operand2 = random.randint(0, 255)

    elif command_operation_id == 1:
        # defLedPin=
        command_operand2 = random.randint(0, 255)

    elif command_operation_id == 2 or command_operation_id == 6 or command_operation_id == 7:
        # tone (tonel, toneb)
        command_operand2 = 0
        command_operand3 = 0
        if random.randint(0,1):
           command_operand2 = random.randint(0, 255)
        if random.randint(0,1):
            command_operand3 = random.randint(0, 4095)

        command_operand4 = random.randint(0, 65535)
    
    elif command_operation_id == 3:
        # noTone
        command_operand2 = 0
        if random.randint(0,1):
            command_operand2 = random.randint(0, 255)

    elif command_operation_id == 4:
        # wait
        command_operand4 = random.randint(0, 65535)

    elif command_operation_id == 5:
        # toggleLed
        command_operand2 = 0
        if random.randint(0,1):
            command_operand2 = random.randint(0, 255)
        
    elif command_operation_id == 15:
        # stop
        pass
    
    else:
        return False
    

    # Всё, собираем команду и возвращаем

    command_operation_id = "[yellow]" + to_hex(command_operation_id, 1) + "[/yellow]"

    command = command_operation_id
    if not command_operand2 == None:
        command_operand2 = "[blue]" + to_hex(command_operand2, 2) + "[/blue]"
        command += command_operand2
    if not command_operand3 == None:
        command_operand3 = "[cyan]" + to_hex(command_operand3, 3) + "[/cyan]"
        command += command_operand3
    if not command_operand4 == None:
        command_operand4 = "[blue]" + to_hex(command_operand4, 4) + "[/blue]"
        command += command_operand4

    return command


def main():
    print("Щас Боженька создаст для вас мелодию.")

    print("Уже просим его...")
    
    output_string = ""
    get_command_return = ""

    while True:
        get_command_return = get_command()
        if not random.randint(1,100) == 100:
            if get_command_return:
                output_string += get_command_return
        else:
            break
    
    console.print(f"Это есть Божья мелодия:\n{output_string}")
    if output_string == "":
        console.print("[bright_black]Похоже Боженька не желает делать для вас музыку сейчас... :([/bright_black]")

if __name__ == '__main__':
    main()

# Я ненавижу Python. И Loxteam тоже.
