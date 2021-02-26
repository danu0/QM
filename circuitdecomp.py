import numpy as np

class Circuit_decomp:

    def __init__(self, U_given):
        '''U given as NxN np array'''
        self.U = U_given

    def unitary_check(self):
        '''Checks if given U is indeed unitary'''
        print(self.U)
        U_transpose = self.U.transpose()
        print(np.matmul(U_transpose, U))
        left_hand_side = np.array_equal(np.matmul(U_transpose, U), np.identity(4))
        right_hand_side = np.array_equal(np.matmul(U, U_transpose), np.identity(4))
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
                    if i != j and U[i][j] != 0:
                        return (i,j)
        else:
            pass




if __name__ == '__main__':
    U = np.array([[0,0,0,1],
                  [0,0,1,0],
                  [0,1,0,0],
                  [1,0,0,0]])
    #print(Circuit_decomp(U).unitary_check())
    print(Circuit_decomp(U).find_non_identity())