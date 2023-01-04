alph = ["A", "B", "C"]
lst= ['A0', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'B0', 'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'C0', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8']
brd = {'A0': 0, 'A1': 1, 'A2': 2, 'A3': 3, 'A4': 4, 'A5': 5, 'A6': 6, 'A7': 7, 'A8': 8, 'B0': 0, 'B1': 1, 'B2': 2, 'B3': 3, 'B4': 4, 'B5': 5, 'B6': 6, 'B7': 7, 'B8': 8, 'C0': 0, 'C1': 1, 'C2': 2, 'C3': 3, 'C4': 4, 'C5': 5, 'C6': 6, 'C7': 7, 'C8': 8}
if alph[0] == 'A' and len(alph) > 1:
    print('A', end='      ')
if len(alph) == 1 and alph[0] == 'A':
    print('A', end='')
    print()
if len(alph) == 3 and alph[1] == 'B':
    print('B', end='      ')
if len(alph) == 2 and alph[0] == 'B':
    print('B', end='      ')
if len(alph) == 2 and alph[1] == 'B':
    print('B', end='')
    print()
if len(alph) == 1 and alph[0] == 'B':
    print('B', end='')
    print()
if len(alph) == 3 and alph[2] == 'C':
    print('C')
if len(alph) == 2 and alph[1] == 'C':
    print('C')
if len(alph) == 1 and alph[0] == 'C':
    print('C')
for x in range(0, 9, 3):
    for i in range(3):
        gap = 1
        for j in range(x, x + 3):
            if gap < 3:
                print(brd[(alph[i] + str(j))], end=" ")
                gap += 1
            else:
                print(brd[(alph[i] + str(j))], end="  ")
    print()

def printboard():
    if alph[0] == 'A' and len(alph) > 1:
        print('A', end='      ')
    if len(alph) == 1 and alph[0] == 'A':
        print('A', end='')
        print()
    if len(alph) == 3 and alph[1] == 'B':
        print('B', end='      ')
    if len(alph) == 2 and alph[0] == 'B':
        print('B', end='      ')
    if len(alph) == 2 and alph[1] == 'B':
        print('B', end='')
        print()
    if len(alph) == 1 and alph[0] == 'B':
        print('B', end='')
        print()
    if len(alph) == 3 and alph[2] == 'C':
        print('C')
    if len(alph) == 2 and alph[1] == 'C':
        print('C')
    if len(alph) == 1 and alph[0] == 'C':
        print('C')
    for x in range(0, 9, 3):
        t= 1
        for i in range(len(alph)):
            gap = 1
            for j in range(x, x + 3):
                if gap < 3:
                    print(brd[(alph[i] + str(j))], end=" ")
                    gap += 1
                else:
                    if t< len(alph):
                        print(brd[(alph[i] + str(j))], end="  ")
                        t+=1
                    else:
                        print(brd[(alph[i] + str(j))], end="")
        print()




def deletable():
    for i in alph:
        if ((brd[i + str(0)] == 'X') and (brd[i + str(4)] == 'X') and (brd[i + str(8)] == 'X')) or ((brd[i + str(2)] == 'X') and (brd[i + str(4)] == 'X') and (brd[i + str(6)] == 'X')):
            if i in alph:
                alph.remove(i)
                return True
            else:
                continue
        for j in range(0, 9, 3):
            row1 = 0
            for p in range(j, j + 3):
                if (brd[i + str(p)] == 'X'):
                    row1 += 1
                    if row1 == 3:
                        if i in alph:
                            alph.remove(i)
                            return True
                        else:
                            continue
        for j in range(0, 3):
            column1 = 0
            for p in range(j, j + 7, 3):
                if (brd[i + str(p)] == 'X'):
                    column1 += 1
                    if column1 == 3:
                        if i in alph:
                            alph.remove(i)
                            return True
                        else:
                            continue


def computer():
    edge = 0
    tester = 0
    if brd['A4'] == 4 and brd['B4']== 4 and brd['C4'] == 4 :
        print('Player 1: A4')
        brd['A4'] = 'X'
        printboard()
        return
    if len(alph) == 3 and player2[0:1] == 'A' and round == 1:
        y = int(player2[-1:0:-1])
        if y == 0:
            letter = "A" + str(8)
            if brd[letter] != 'X':
                brd[letter] = 'X'
                print(f'Player 1: {letter}')
                deletable()
                printboard()
                return
        elif y == 1:
            letter = "A" + str(7)
            if brd[letter] != 'X':
                brd[letter] = 'X'
                print(f'Player 1: {letter}')
                deletable()
                printboard()
                return
        elif y == 2:
            letter = "A" + str(6)
            if brd[letter] != 'X':
                brd[letter] = 'X'
                print(f'Player 1: {letter}')
                deletable()
                printboard()
                return
        elif y == 5:
            letter = "A" + str(3)
            if brd[letter] != 'X':
                brd[letter] = 'X'
                print(f'Player 1: {letter}')
                deletable()
                printboard()
                return
        elif y == 3:
            letter = "A" + str(5)
            if brd[letter] != 'X':
                brd[letter] = 'X'
                print(f'Player 1: {letter}')
                deletable()
                printboard()
                return
        elif y == 6:
            letter = "A" + str(2)
            if brd[letter] != 'X':
                brd[letter] = 'X'
                print(f'Player 1: {letter}')
                deletable()
                printboard()
                return
        elif y == 7:
            letter = "A" + str(1)
            if brd[letter] != 'X':
                brd[letter] = 'X'
                print(f'Player 1: {letter}')
                deletable()
                printboard()
                return
        elif y == 8:
            letter = "A" + str(0)
            if brd[letter] != 'X':
                brd[letter] = 'X'
                print(f'Player 1: {letter}')
                deletable()
                printboard()
                return
        return
    if len(alph) == 3 and (player2[0:1]== 'B' or player2[0:1] == 'C') and round == 1:
        if player2[0:1] == 'B':
            print('Player 1: C4')
            global myboard
            myboard = 'C'
            brd['C4'] = 'X'
            printboard()
            return
        elif player2[0:1] == 'C':
            print('Player 1: B4')
            myboard = 'B'
            brd['B4'] = 'X'
            printboard()
            return
    if len(alph) == 3 and round == 2 and player2[:1] != myboard:
        count = 0
        for i in range(0, 9, 4):
            if brd[player2[:1] + str(i)] == 'X':
                count += 1
                if count == 2:
                    for j in range(0, 9, 4):
                        if brd[player2[:1] + str(j)] != 'X':
                            letter = player2[:1] + str(j)
                            brd[player2[:1] + str(j)] = 'X'
                            print(f'Player 1: {letter}')
                            deletable()
                            printboard()
                            return True

            count = 0
            for i in range(2, 9, 2):
                if brd[player2[:1] + str(i)] == 'X':
                    count += 1
                    if count == 2:
                        for j in range(2, 9, 4):
                            if brd[player2[:1] + str(j)] != 'X':
                                letter = player2[:1] + str(j)
                                brd[player2[:1] + str(j)] = 'X'
                                print(f'Player 1: {letter}')
                                deletable()
                                printboard()
                                return True
            for j in range(0, 9, 3):
                row1 = 0
                for p in range(j, j + 3):
                    if (brd[player2[:1] + str(p)] == 'X'):
                        row1 += 1
                        if row1 == 2:
                            for a in range(0, 9, 3):
                                for b in range(a, a + 3):
                                    if brd[player2[:1] + str(b)] != 'X':
                                        letter = player2[:1] + str(b)
                                        brd[player2[:1] + str(b)] = 'X'
                                        print(f'Player 1: {letter}')
                                        deletable()
                                        printboard()
                                        return True
        else:
             count = 0
             for j in range(0, 3):
                 column1 = 0
                 for p in range(j, j + 7, 3):
                     if (brd[player2[:1] + str(p)] == 'X'):
                         count += 1
                         break
                     else:
                         column1 += 1
                         if column1 == 3:
                             empty_column = j
             newcount = 0
             if count == 2:
                 for v in range(0, 9, 3):
                     row_1 = 0
                     for n in range(v, v + 3):
                         if (brd[player2[:1] + str(n)] == 'X'):
                             newcount += 1
                             break
                         else:
                             row1 += 1
                             if row1 == 3:
                                 empty_row = v
             if newcount == 2:
                 y = empty_row + empty_column
                 letter = player2[:1] + str(y)
                 brd[letter] = 'X'
                 print(f' Player 1: {letter}')
                 printboard()
                 return True
    if len(alph) == 3 and round == 2 and player2[:1] == myboard:
        myboard = 'A'
        count = 0
        for i in range(0, 9, 4):
            if brd[player2[:1] + str(i)] == 'X':
                count += 1
                if count == 2:
                    for j in range(0, 9, 4):
                        if brd[player2[:1] + str(j)] != 'X':
                            letter = player2[:1] + str(j)
                            brd[player2[:1] + str(j)] = 'X'
                            print(f'Player 1: {letter}')
                            deletable()
                            printboard()
                            return True

            count = 0
            for i in range(2, 9, 2):
                if brd[player2[:1] + str(i)] == 'X':
                    count += 1
                    if count == 2:
                        for j in range(2, 9, 4):
                            if brd[player2[:1] + str(j)] != 'X':
                                letter = player2[:1] + str(j)
                                brd[player2[:1] + str(j)] = 'X'
                                print(f'Player 1: {letter}')
                                deletable()
                                printboard()
                                return True
            for j in range(0, 9, 3):
                row1 = 0
                for p in range(j, j + 3):
                    if (brd[player2[:1] + str(p)] == 'X'):
                        row1 += 1
                        if row1 == 2:
                            for a in range(0, 9, 3):
                                for b in range(a, a + 3):
                                    if brd[player2[:1] + str(b)] != 'X':
                                        letter = player2[:1] + str(b)
                                        brd[player2[:1] + str(b)] = 'X'
                                        print(f'Player 1: {letter}')
                                        deletable()
                                        printboard()
                                        return True

    if len(alph) == 3 and round == 3 and player2[:1] != myboard:
        count = 0
        for i in range(0, 9, 4):
            if brd[player2[:1] + str(i)] == 'X':
                count += 1
                if count == 2:
                    for j in range(0, 9, 4):
                        if brd[player2[:1] + str(j)] != 'X':
                            letter = player2[:1] + str(j)
                            brd[player2[:1] + str(j)] = 'X'
                            print(f'Player 1: {letter}')
                            deletable()
                            printboard()
                            return True

        count = 0
        for i in range(2, 9, 2):
            if brd[player2[:1] + str(i)] == 'X':
                count += 1
                if count == 2:
                    for j in range(2, 9, 4):
                        if brd[player2[:1] + str(j)] != 'X':
                            letter = player2[:1] + str(j)
                            brd[player2[:1] + str(j)] = 'X'
                            print(f'Player 1: {letter}')
                            deletable()
                            printboard()
                            return True
        for j in range(0, 9, 3):
            row_1 = 0
            for p in range(j, j + 3):
                if (brd[player2[:1] + str(p)] == 'X'):
                    row_1 += 1
                    if row_1 == 2:
                        for a in range(0, 9, 3):
                            for b in range(a, a + 3):
                                if brd[player2[:1] + str(b)] != 'X':
                                    letter = player2[:1] + str(b)
                                    brd[player2[:1] + str(b)] = 'X'
                                    print(f'Player 1: {letter}')
                                    deletable()
                                    printboard()
                                    return True

    if len(alph) == 3 and round == 3 and player2[:1] == myboard:
        myboard = 'A'
        count = 0
        for i in range(0, 9, 4):
            if brd[player2[:1] + str(i)] == 'X':
                count += 1
                if count == 2:
                    for j in range(0, 9, 4):
                        if brd[player2[:1] + str(j)] != 'X':
                            letter = player2[:1] + str(j)
                            brd[player2[:1] + str(j)] = 'X'
                            print(f'Player 1: {letter}')
                            deletable()
                            printboard()
                            return True

        count = 0
        for i in range(2, 9, 2):
            if brd[player2[:1] + str(i)] == 'X':
                count += 1
                if count == 2:
                    for j in range(2, 9, 4):
                        if brd[player2[:1] + str(j)] != 'X':
                            letter = player2[:1] + str(j)
                            brd[player2[:1] + str(j)] = 'X'
                            print(f'Player 1: {letter}')
                            deletable()
                            printboard()
                            break
        for j in range(0, 9, 3):
            row_1 = 0
            for p in range(j, j + 3):
                if (brd[player2[:1] + str(p)] == 'X'):
                    row_1 += 1
                    if row_1 == 2:
                        for a in range(0, 9, 3):
                            for b in range(a, a + 3):
                                if brd[player2[:1] + str(b)] != 'X':
                                    letter = player2[:1] + str(b)
                                    brd[player2[:1] + str(b)] = 'X'
                                    print(f'Player 1: {letter}')
                                    deletable()
                                    printboard()
                                    return True

    if len(alph) == 2 and round == 2:
        if player2[:1] == 'B':
            print('Player 1: C4')
            myboard = 'C'
            brd['C4'] = 'X'
            printboard()
            return
        elif player2[:1] == 'C':
            print('Player 1: B4')
            myboard = 'B'
            brd['B4'] = 'X'
            printboard()
            return
    if len(alph) == 2 and round != 2 and player2[:1] != myboard:
        tek= False
        if tek== False:
            count = 0
            for i in range(0, 9, 4):
                if brd[player2[:1] + str(i)] == 'X':
                    count += 1
                    if count == 2:
                        for j in range(0, 9, 4):
                            if brd[player2[:1] + str(j)] != 'X':
                                letter = player2[:1] + str(j)
                                brd[player2[:1] + str(j)] = 'X'
                                print(f'Player 1: {letter}')
                                deletable()
                                printboard()
                                tek= True
                                break

            count = 0
            for i in range(2, 9, 2):
                if brd[player2[:1] + str(i)] == 'X':
                    count += 1
                    if count == 2:
                        for j in range(2, 9, 4):
                            if brd[player2[:1] + str(j)] != 'X':
                                letter = player2[:1] + str(j)
                                brd[player2[:1] + str(j)] = 'X'
                                print(f'Player 1: {letter}')
                                deletable()
                                printboard()
                                break
            for j in range(0, 9, 3):
                row_1 = 0
                for p in range(j, j + 3):
                    if (brd[player2[:1] + str(p)] == 'X'):
                        row_1 += 1
                        if row_1 == 2:
                            for a in range(0, 9, 3):
                                for b in range(a, a + 3):
                                    if brd[player2[:1] + str(b)] != 'X':
                                        letter = player2[:1] + str(b)
                                        brd[player2[:1] + str(b)] = 'X'
                                        print(f'Player 1: {letter}')
                                        deletable()
                                        printboard()
                                        tek= True
                                        break

        else:
            count = 0
            for j in range(0, 3):
                column_1 = 0
                for p in range(j, j + 7, 3):
                    if (brd[player2[:1] + str(p)] == 'X'):
                        count += 1
                        break
                    else:
                        column_1 += 1
                        if column_1 == 3:
                                empty_column = j
            new_count = 0
            if count == 2:
                for v in range(0, 9, 3):
                    row_1 = 0
                    for n in range(v, v + 3):
                        if (brd[player2[:1] + str(n)] == 'X'):
                            new_count += 1
                            break
                        else:
                            row_1 += 1
                            if row_1 == 3:
                                empty_row = v
            if new_count == 2:
                y = empty_row + empty_column
                letter = player2[:1] + str(y)
                brd[letter] = 'X'
                print(f' Player 1: {letter}')
                printboard()
                return

    if len(alph) == 2 and brd[alph[0] + str(4)] == 'X' and brd[alph[1] + str(4)] == 'X' and player2[:1] == myboard: #new
        count = 0
        for i in range(0, 9, 4):
            if brd[player2[:1] + str(i)] == 'X':
                count += 1
                if count == 2:
                    for j in range(0, 9, 4):
                        if brd[player2[:1] + str(j)] != 'X':
                            letter = player2[:1] + str(j)
                            brd[player2[:1] + str(j)] = 'X'
                            print(f'Player 1: {letter}')
                            deletable()
                            printboard()
                            break

        count = 0
        for i in range(2, 9, 2):
            if brd[player2[:1] + str(i)] == 'X':
                count += 1
                if count == 2:
                    for j in range(2, 9, 4):
                        if brd[player2[:1] + str(j)] != 'X':
                            letter = player2[:1] + str(j)
                            brd[player2[:1] + str(j)] = 'X'
                            print(f'Player 1: {letter}')
                            deletable()
                            printboard()
                            break
        for j in range(0, 9, 3):
            row_1 = 0
            for p in range(j, j + 3):
                if (brd[player2[:1] + str(p)] == 'X'):
                    row_1 += 1
                    if row_1 == 2:
                        for a in range(0, 9, 3):
                            for b in range(a, a + 3):
                                if brd[player2[:1] + str(b)] != 'X':
                                    letter = player2[:1] + str(b)
                                    brd[player2[:1] + str(b)] = 'X'
                                    print(f'Player 1: {letter}')
                                    deletable()
                                    printboard()
                                    break

        myboard = alph[0] #new
        return
    if len(alph) == 2 and player2[:1] == myboard:
        if player2 != brd[myboard + '4']:
            y = int(player2[-1:0:-1]) + 5
            if y <= 8 and brd[myboard + str(y)] != 'X':
                letter = myboard + str(y)
                brd[letter] = 'X'
                print(f'player 1: {letter}')
                printboard()
                return
            elif y > 8 and brd[myboard + str(y - 10)] != 'X':
                 y = y - 10
                 letter = myboard + str(y)
                 brd[letter] = 'X'
                 print(f'player 1: {letter}')
                 printboard()
                 return
            elif brd[myboard + str(y)] == 'X':
                 y = y - 5
                 if y == 1:
                     letter = myboard + str(8)
                     brd[letter] = 'X'
                     print(f'player 1: {letter}')
                     printboard()
                     return
                 elif y == 3:
                     letter = myboard + str(2)
                     brd[letter] = 'X'
                     print(f'player 1: {letter}')
                     printboard()
                     return
                 elif y == 5:
                     letter = myboard + str(6)
                     brd[letter] = 'X'
                     print(f'player 1: {letter}')
                     printboard()
                     return
                 elif y == 7:
                      letter = myboard + str(0)
                      brd[letter] = 'X'
                      print(f'player 1: {letter}')
                      printboard()
                      return
                 elif y == 8:
                      letter = myboard + str(1)
                      brd[letter] = 'X'
                      print(f'player 1: {letter}')
                      printboard()
                      return
                 elif y == 0:
                      letter = myboard + str(7)
                      brd[letter] = 'X'
                      print(f'player 1: {letter}')
                      printboard()
                      return
                 elif y == 6:
                      letter = myboard + str(5)
                      brd[letter] = 'X'
                      print(f'player 1: {letter}')
                      printboard()
                      return
    if len(alph) == 1 and player2[:1] == myboard and (myboard in alph):
                   if player2 != brd[player2[:1] + '4']:

                       y = int(player2[-1:0:-1]) + 5
                       if y <= 8 and brd[player2[:1] + str(y)] != 'X':
                           letter = player2[:1] + str(y)
                           brd[letter] = 'X'
                           print(f'player 1: {letter}')
                           printboard()
                           return
                       elif y > 8 and brd[player2[:1] + str(y - 10)] != 'X':
                           y = y - 10
                           letter = player2[:1] + str(y)
                           brd[letter] = 'X'
                           print(f'player 1: {letter}')
                           printboard()
                           return
                       elif brd[player2[:1] + str(y)] == 'X':
                           y = y - 5
                           if y == 1:
                               letter = player2[:1] + str(8)
                               brd[letter] = 'X'
                               print(f'player 1: {letter}')
                               printboard()
                               return
                           elif y == 3:
                               letter = player2[:1] + str(2)
                               brd[letter] = 'X'
                               print(f'player 1: {letter}')
                               printboard()
                               return
                           elif y == 5:
                               letter = player2[:1] + str(6)
                               brd[letter] = 'X'
                               print(f'player 1: {letter}')
                               printboard()
                               return
                           elif y == 7:
                               letter = player2[:1] + str(0)
                               brd[letter] = 'X'
                               print(f'player 1: {letter}')
                               printboard()
                               return
                           elif y == 8:
                               letter = player2[:1] + str(1)
                               brd[letter] = 'X'
                               print(f'player 1: {letter}')
                               printboard()
                               return
                           elif y == 0:
                               letter = player2[:1] + str(7)
                               brd[letter] = 'X'
                               print(f'player 1: {letter}')
                               printboard()
                               return
                           elif y == 6:
                               letter = player2[:1] + str(5)
                               brd[letter] = 'X'
                               print(f'player 1: {letter}')
                               printboard()
                               return
    if len(alph) == 1 and (player2[:1] != myboard or (myboard not in alph)) and edge == 0:
       letter = alph[0]
       number_axes = 0
       for i in range(0, 9):
           if brd[letter + str(i)] == 'X':
               number_axes += 1
       if number_axes > 1 and tester == 0:
           if brd[letter + str(0)] == 'X' and brd[letter + str(8)] != 'X':
               y = letter + str(8)
               brd[y] = 'X'
               print(f'Player 1: {y}')
               corner = 1
               printboard()
               return
   
           elif brd[letter + str(2)] == 'X' and brd[letter + str(6)] != 'X':
               y = letter + str(6)
               brd[y] = 'X'
               print(f'Player 1: {y}')
               corner = 1
               printboard()
               return
           elif brd[letter + str(6)] == 'X' and brd[letter + str(2)] != 'X':
               y = letter + str(2)
               brd[y] = 'X'
               print(f'Player 1: {y}')
               corner = 1
               printboard()
               return
           elif brd[letter + str(8)] == 'X' and brd[letter + str(0)] != 'X':
               y = letter + str(0)
               brd[y] = 'X'
               print(f' Player 1: {y}')
               corner = 1
               printboard()
               return
       else:
           if brd[letter + str(0)] == 'X' and brd[letter + str(8)] != 'X':
               y = letter + str(8)
               brd[y] = 'X'
               print(f' Player 1: {y}')
               tester += 1
               printboard()
               return
           elif brd[letter + str(2)] == 'X' and brd[letter + str(6)] != 'X':
               y = letter + str(6)
               brd[y] = 'X'
               print(f' Player 1: {y}')
               tester += 1
               printboard()
               return
   
           elif brd[letter + str(6)] == 'X' and brd[letter + str(2)] != 'X':
               y = letter + str(2)
               brd[y] = 'X'
               print(f' Player 1: {y}')
               tester += 1
               printboard()
               return
   
           elif brd[letter + str(8)] == 'X' and brd[letter + str(0)] != 'X':
               y = letter + str(0)
               brd[y] = 'X'
               print(f'Player 1: {y}')
               tester += 1
               printboard()
               return
           elif brd[letter + str(1)] == 'X' and brd[letter + str(7)] != 'X':
               y = letter + str(7)
               brd[y] = 'X'
               print(f' Player 1: {y}')
               tester += 1
               printboard()
               return
           elif brd[letter + str(7)] == 'X' and brd[letter + str(1)] != 'X':
               y = letter + str(1)
               brd[y] = 'X'
               print(f' Player 1: {y}')
               tester += 1
               printboard()
               return
   
           elif brd[letter + str(3)] == 'X' and brd[letter + str(5)] != 'X':
               y = letter + str(5)
               brd[y] = 'X'
               print(f'Player 1: {y}')
               tester += 1
               printboard()
               return
   
           elif brd[letter + str(5)] == 'X' and brd[letter + str(3)] != 'X':
               y = letter + str(3)
               brd[y] = 'X'
               print(f' Player 1: {y}')
               tester += 1
               printboard()
               return
    if (len(alph) == 1 and (player2[:1] != myboard or (myboard not in letter)) and edge == 1):
        for v in range(1,8,2):
            alphabet = alph[v]
            c = alphabet + str(v)
            if brd[c] != 'X':
                brd[c] = 'X'
                print(f' Player 1: {c}')
                printboard()
                return




game = False
round = 0
while game == False:
    if game == True:
        break
    test = True
    while test == True:
        computer()
        test = False
    if game==True:
        break
    test = True
    while test == True:
        player2 = input('Player 2: ')
        if (player2 in lst) and (brd[player2] != 'X') and (player2[:1] in alph):
            round += 1
            brd[player2] = 'X'
            if len(alph) == 1 and deletable() == True:
                print('Player 1 wins game')
                game = True
                test = False
                break
            else:
                deletable()
                printboard()
                test = False
        else:
            print('Invalid move, please input again')
