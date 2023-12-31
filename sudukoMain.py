from utlis import *
import sudukoSolver

########################################################################
heightImg = 450
widthImg = 450
model = intializePredectionModel()  # LOAD THE CNN MODEL
########################################################################

def solve_sudoku(pathImage):
    
    # preparing the image
    img = cv2.imread(pathImage)
    img = cv2.resize(img, (widthImg, heightImg))  
    imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)  
    imgThreshold = preProcess(img)

    #  Finding all contours
    imgContours = img.copy()
    imgBigContour = img.copy() 
    contours, hierarchy = cv2.findContours(imgThreshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) 
    cv2.drawContours(imgContours, contours, -1, (0, 255, 0), 3) 

    #Finding the biggest contour which is sudoku board
    biggest, maxArea = biggestContour(contours) # FIND THE BIGGEST CONTOUR
    print(biggest)
    if biggest.size != 0:
        biggest = reorder(biggest)
        print(biggest)
        cv2.drawContours(imgBigContour, biggest, -1, (0, 0, 255), 25) 
        pts1 = np.float32(biggest) 
        pts2 = np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) 
        matrix = cv2.getPerspectiveTransform(pts1, pts2) # GER
        imgWarpColored = cv2.warpPerspective(img, matrix, (widthImg, heightImg))
        imgDetectedDigits = imgBlank.copy()
        imgWarpColored = cv2.cvtColor(imgWarpColored,cv2.COLOR_BGR2GRAY)

        #splitting the image and predicting each box
        imgSolvedDigits = imgBlank.copy()
        boxes = splitBoxes(imgWarpColored)
        print(len(boxes))
        numbers = getPredection(boxes, model)
        print(numbers)
        imgDetectedDigits = displayNumbers(imgDetectedDigits, numbers, color=(255, 0, 255))
        numbers = np.asarray(numbers)
        posArray = np.where(numbers > 0, 0, 1)
        print(posArray)


        #Using sudoku solver logic
        board = np.array_split(numbers,9)
        print(board)
        try:
            sudukoSolver.solve(board)
        except:
            pass
        print(board)
        flatList = []
        for sublist in board:
            for item in sublist:
                flatList.append(item)
        solvedNumbers =flatList*posArray
        imgSolvedDigits= displayNumbers(imgSolvedDigits,solvedNumbers)

        
        pts2 = np.float32(biggest) 
        pts1 =  np.float32([[0, 0],[widthImg, 0], [0, heightImg],[widthImg, heightImg]]) 
        matrix = cv2.getPerspectiveTransform(pts1, pts2)  # GER
        imgInvWarpColored = img.copy()
        imgInvWarpColored = cv2.warpPerspective(imgSolvedDigits, matrix, (widthImg, heightImg))
        inv_perspective = cv2.addWeighted(imgInvWarpColored, 1, img, 0.5, 1)
        imgDetectedDigits = drawGrid(imgDetectedDigits)
        imgSolvedDigits = drawGrid(imgSolvedDigits)

        return inv_perspective #solved image

    else:
        print("No Sudoku Found")
