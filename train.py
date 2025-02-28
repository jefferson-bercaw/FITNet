from trainUtil.trainingUtil import TrainUtil
from data.readDataFromExcel import getDataFromExcelFile as getOCTFile
import os

if __name__ == '__main__':
    dataSetName = 'ACL'
    kFold = 10
    classNumber = 2
    imgSize = 224
    epoch_num = 100
    baseLR = 1e-3
    lr_scheduler = 'step'
    gpuNumber = "cuda:4"
    lossName = 'crossEntropyLoss'   # or 'focalLoss'
    optimizer = 'SGD'
    # Set the threshold for saving the model
    saveValAcc = 50.0
    saveModelNumber = 1

    cur_dir = os.getcwd()

    encoder = 'FITNet'
    imgDataRoot = cur_dir + '/subset_data/2D_Images'
    trainExcelFilePath = cur_dir + '/data/Fold_Split.xlsx'
    resultRootPath = cur_dir + '/data/10FoldResult'

    fold = int(os.environ['SLURM_ARRAY_TASK_ID'])
    # for fold in range(kFold):

    trainExcelSheetName = 'train_fold{}'.format(fold)
    validExcelSheetName = 'valid_fold{}'.format(fold)

    trainExcelSheetName = 'train_fold{}'.format(fold)
    validExcelSheetName = 'valid_fold{}'.format(fold)

    training = TrainUtil(dataSetName=dataSetName, classNumber=classNumber, trainDataRoot=trainExcelSheetName,
                         validDataRoot=validExcelSheetName, encoder=encoder, getDataFunc=getOCTFile,
                         resultRootPath=resultRootPath, baseLR=baseLR, lr_scheduler=lr_scheduler,
                         gpuNumber=gpuNumber, saveValAcc=saveValAcc, saveModelNumber=saveModelNumber,
                         lossName=lossName, optimizer=optimizer, imgSize=imgSize, epoch_num=epoch_num,
                         imgDataRoot=imgDataRoot, trainExcelFilePath=trainExcelFilePath,
                         fold=fold)
    training.running()
