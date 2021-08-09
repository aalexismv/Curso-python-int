import random
import os


def read_data(filepath="./archivos/data.txt"):
    words = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f:
            words.append(line.strip().upper())
    return words

def run():
    data = read_data(filepath="./archivos/data.txt")
    chosen_word = random.choice(data)
    chosen_word_list = [letter for letter in chosen_word]
    chosen_word_list_underscores = ["_"] * len(chosen_word_list)
    letter_index_dict = {}
    for idx, letter in enumerate(chosen_word):
        if not letter_index_dict.get(letter):
            letter_index_dict[letter] = []
        letter_index_dict[letter] .append(idx)

    while True:
        os.system("cls")
        print("""
   _     _     _     _     _     _     _     _     _     _     _     _  
  / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \   / \ 
 ( ¡ ) ( B ) ( i ) ( e ) ( n ) ( v ) ( e ) ( n ) ( i ) ( d ) ( @ ) ( ! )
  \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/   \_/ 
                                   _                                    
                                  / \                                   
                                 ( a )                                  
                                  \_/                                   
                 _     _     _     _     _     _     _                  
                / \   / \   / \   / \   / \   / \   / \                 
               ( H ) ( A ) ( N ) ( G ) ( M ) ( A ) ( N )                
                \_/   \_/   \_/   \_/   \_/   \_/   \_/                 
            Adivina la palabra
            """)
        for element in chosen_word_list_underscores:
            print(element + "", end="")
        print("\n")

        letter = input("Ingresa una letra: ").strip().upper()
        assert letter.isalpha(), "Solo puedes ingresar letras"

        if letter in chosen_word_list:
            for idx in letter_index_dict[letter]:
                chosen_word_list_underscores[idx] = letter

        if "_" not in chosen_word_list_underscores:
            os.system("cls")
            print("""
                            ⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
                            ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
                            ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
                            ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                            ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                             ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
                            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉
   .g8MMMbgd       db      `7MN.   `7MF'    db       .MMMMbgd MMP""MM""YMM `7MMMMMYMM  
.dP'     `M      ;MM:       MMN.    M      ;MM:     ,MI    "Y P'   MM   `7   MM    `7  
dM'       `     ,V^MM.      M YMb   M     ,V^MM.    `MMb.          MM        MM   d    
MM             ,M  `MM      M  `MN. M    ,M  `MM      `YMMNq.      MM        MMmmMM    
MM.    `7MMF'  AbmmmqMA     M   `MM.M    AbmmmqMA   .     `MM      MM        MM   Y  , 
`Mb.     MM   A'     VML    M     YMM   A'     VML  Mb     dM      MM        MM     ,M 
  `"bmmmdPY .AMA.   .AMMA..JML.    YM .AMA.   .AMMA.P"Ybmmd"     .JMML.    .JMMmmmmMMM   
---------------------------------------------------------------------------------------
            """)
            print("¡Ganaste! La palabra era", chosen_word)
            break

if __name__ == '__main__':
    run()