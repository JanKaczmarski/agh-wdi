# zadanie 9

# 3 5 7 ...

def main(T, k):
	N = len(T)
	for i in range(N-2):
		for j in range(N-2):
			m = 2
			while i + m < N and j + m < N:
				if T[i][j] * T[j][j + m] * T[i + m][j] * T[i + m][j + m] == k:
					return True, (i + m/2, j + m/2)
				m += 2
	return False


if __name__ == "__main__":
	print(main([[1,0,1,1,1],[0,0,0,0,1],[1,0,1,1,1],[1,1,1,1,1],[1,1,1,1,100]], 100))
 