def convert_to_upper(string):
    newstring = ""
    for letter in string:
        newstring += letter.upper()
    return newstring

string = input("Send_maze Send_foreign_pacman_arrived Send_foreign_pacman_left Send_foreign_pacman_died Send_pacman_go_home Send_pacman_update Send_ghost_update Send_foreign_pacman_ate_ghost Send_eat Send_score_update Send_lives_update Send_status_update ")
output = convert_to_upper(string)
print(output)
