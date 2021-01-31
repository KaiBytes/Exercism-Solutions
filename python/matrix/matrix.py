class Matrix:
    #constructor
    def __init__(self, matrix_string):
        self.matrix = [[int(e) for e in row.split()] for row in matrix_string.split("\n")]

    #getter
    def row(self, index):
        return self.matrix[index - 1]               

    #getter
    def column(self, index):
        return [row[index - 1] for row in self.matrix]
    
                
                

