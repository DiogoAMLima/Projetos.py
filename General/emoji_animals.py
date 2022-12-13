import emoji

print('\033[31mLista dos animais: Lagarto - 1, Dragão - 2, Pássaro - 3, Águia - 4, Macaco - 5, Cobra - 6,\n '
      'Gato - 7, Polvo - 8, Tigre - 9, Gorila - 10, Elefante - 11, Crocodilo - 12, Leão - 13, Cachorro - 14,\n '
      'Golfinho - 15\033[m')

while True:
    esc = int(input('\nEscolha um dos animais na lista: '))
    match esc:
        case 1:
            print(emoji.emojize('\n\033[31mLagarto: :lizard:\033[m'))
        case 2:
            print(emoji.emojize('\n\033[32mDragão: :dragon:\033[m'))
        case 3:
            print(emoji.emojize('\n\033[33mPássaro: :bird:\033[m'))
        case 4:
            print(emoji.emojize('\n\033[34mÁguia: :eagle:\033[m'))
        case 5:
            print(emoji.emojize('\n\033[35mMacaco: :monkey:\033[m'))
        case 6:
            print(emoji.emojize('\n\033[36mCobra: :snake:\033[m'))
        case 7:
            print(emoji.emojize('\n\033[37mGato: :cat:\033[m'))
        case 8:
            print(emoji.emojize('\n\033[97mPolvo: :octopus:\033[m'))
        case 9:
            print(emoji.emojize('\n\033[31mTigre: :tiger:\033[m'))
        case 10:
            print(emoji.emojize('\n\033[32mGorila: :gorilla:\033[m'))
        case 11:
            print(emoji.emojize('\n\033[33mElefante: :elephant:\033[m'))
        case 12:
            print(emoji.emojize('\n\033[34mCrocodilo: :crocodile:\033[m'))
        case 13:
            print(emoji.emojize('\n\033[35mLeão: :lion:\033[m'))
        case 14:
            print(emoji.emojize('\n\033[36mCachorro: :dog:\033[m'))
        case 15:
            print(emoji.emojize('\nGolfinho: :dolphin:'))
    op = str(input('\nDeseja ver outro emoji? [S/N]? ')).strip().upper()
    if op in 'S':
        continue
    else:
        print('\n\033[97mAté a próxima!\033[m')
        break
