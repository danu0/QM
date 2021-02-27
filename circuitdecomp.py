import numpy as np

class Circuit_decomp:

    def __init__(self, U_given):
        '''U given as NxN np array'''
        self.U = U_given

    def unitary_check(self):
        '''Checks if given U is indeed unitary'''
        U_transpose = self.U.transpose()
        left_hand_side = np.array_equal(np.matmul(U_transpose, U), np.identity(self.U.shape[0]))
        right_hand_side = np.array_equal(np.matmul(U, U_transpose), np.identity(self.U.shape[0]))
        if left_hand_side and right_hand_side :
            return True
        else:
            raise Exception("Please enter a unitary matrix!")

    def find_non_identity(self):
        '''
        Finds a non diagonal element not equal to 0
        :return: First element in column (not on the diagonal) not equal to 0
        '''
        if Circuit_decomp(self.U).unitary_check():
            for i in range(0,(self.U.shape[0])):
                for j in range(0,self.U.shape[1]):
                    if i != j and U[j][i] != 0:
                        return (j,i)
        else:
            pass

    def calculate_next_U(self):
        i, j = Circuit_decomp(self.U).find_non_identity()
        X = np.identity(self.U.shape[0])
        if self.U[i][i] == 0 and self.U[i][j] != 0:
            X[j][j] = 0
            X[i][i] = 0
            X[i][j]= 1
            X[j][i]= 1
        else:
            X[j][j] = np.sqrt( 1 / (self.U[j][i] / self.U[i][i])**2 + 1 )
            X[i][i] = X[j][j]
            X[i][j] = np.sqrt(1 - (X[j][j])**2)
            X[j][i] = np.sqrt(1 - (X[j][j])**2)
        return X

    def decomp_algorithm(self):
        X = Circuit_decomp(self.U).calculate_next_U()
        lst_of_unitaries = [X]
        next = np.matmul(X, self.U)
        print(X)
        print(next)
        test = Circuit_decomp(next).unitary_check()
        '''
        while not np.array_equal(next, np.identity(self.U.shape[0])):
            next = Circuit_decomp(next).calculate_next_U()
            lst_of_unitaries.append(next)
        '''
        return lst_of_unitaries


if __name__ == '__main__':
    U = np.array([[0,0,0,1],
                  [0,0,1,0],
                  [0,1,0,0],
                  [1,0,0,0]])
    #print(Circuit_decomp(U).unitary_check())
    print(Circuit_decomp(U).find_non_identity())
    x = Circuit_decomp(U).decomp_algorithm()
    #print(x)