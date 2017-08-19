import pandas
import numpy as np

def make_vector(values, value):
    ret = np.zeros(values.size)
    for i in range(values.size):
        if value == values[i]:
            ret[i] = 1
            break
    return ret


def Id(value):
    return value

# Identifies the type of dwelling involved in the sale.
def MSSubClass(value):
    return make_vector(np.array([20,30,40,45,50,60,70,75,80,85,90,120,150,160,180,190]), value)

# Identifies the general zoning classification of the sale.
def MSZoning(value):
    return make_vector(np.array(['A','C','FV','I','RH','RL','RP','RM']), value)

# Linear feet of street connected to property
def LotFrontage(value):
    return value

# Lot size in square feet
def LotArea(value):
    return value

# Type of road access to property
def Street(value):
    return make_vector(np.array(['Grvl', 'Pave']), value)

# Type of alley access to property
def Alley(value):
    return make_vector(np.array(['Grvl', 'Pave', 'NA']), value)

# General shape of property
def LotShape(value):
    return make_vector(np.array(['Reg','IR1','IR2','IR3']), value)
# Flatness of the property
def LandContour(value):
    return make_vector(np.array(['Lvl','Bnk','HLS','Low']), value)

# Type of utilities available
def Utilities(value):
    return make_vector(np.array(['AllPub','NoSewr','NoSeWa','ELO']), value)

# Lot configuration
def LotConfig(value):
    return make_vector(np.array(['Inside','Corner','CulDSac','FR2','FR3']), value)

# Slope of property
def LandSlope(value):
    return make_vector(np.array(['Gtl','Mod','Sev']), value)

# Physical locations within Ames city limits
def Neighborhood(value):
    return make_vector(np.array(['Blmngtn','Blueste','BrDale','BrkSide','ClearCr','CollgCr','Crawfor','Edwards','Gilbert','IDOTRR','MeadowV','Mitchel','Names','NoRidge','NPkVill','NridgHt','NWAmes','OldTown','SWISU','Sawyer','SawyerW','Somerst','StoneBr','Timber','Veenker']), value)

# Proximity to various conditions
def Condition1(value):
    return make_vector(np.array(['Artery','Feedr','Norm','RRNn','RRAn','PosN','PosA','RRNe','RRAe']), value)

# Proximity to various conditions (if more than one is present)
def Condition2(value):
    return make_vector(np.array(['Artery','Feedr','Norm','RRNn','RRAn','PosN','PosA','RRNe','RRAe']), value)

# Type of dwelling
def BldgType(value):
    return make_vector(np.array(['1Fam','2FmCon','Duplx','TwnhsE','TwnhsI']), value)

# Style of dwelling
def HouseStyle(value):
    return make_vector(np.array(['1Story','1.5Fin','1.5Unf','2Story','2.5Fin','2.5Unf','SFoyer','SLvl']), value)

# Rates the overall material and finish of the house
def OverallQual(value):
    return value

# Rates the overall condition of the house
def OverallCond(value):
    return value

# Original construction date
def YearBuilt(value):
    return np.array([]) # dont know yet how to use this correctly

# Remodel date (same as construction date if no remodeling or additions)
def YearRemodAdd(value):
    return np.array([]) # dont know yet how to use this correctly

# Type of roof
def RoofStyle(value):
    return make_vector(np.array(['Flat','Gable','Gambrel','Hip','Mansard','Shed']), value)

# Roof material
def RoofMatl(value):
    return make_vector(np.array(['ClyTile', 'CompShg','Membran','Metal','Roll','Tar&Grv','WdShake','WdShngl']), value)

# Exterior covering on house
def Exterior1st(value):
    return make_vector(np.array(['AsbShng','AsphShn','BrkComm','BrkFace','CBlock','CemntBd','HdBoard','ImStucc','MetalSd','Other','Plywood','PreCast','Stone','Stucco','VinylSd','Wd Sdng','WdShing']), value)

# Exterior covering on house (if more than one material)
def Exterior2nd(value):
    return make_vector(np.array(['AsbShng','AsphShn','BrkComm','BrkFace','CBlock','CemntBd','HdBoard','ImStucc','MetalSd','Other','Plywood','PreCast','Stone','Stucco','VinylSd','Wd Sdng','WdShing']), value)

# Masonry veneer type
def MasVnrType(value):
    return make_vector(np.array(['BrkCmn','BrkFace','CBlock','None','Stone']), value)

# Masonry veneer area in square feet
def MasVnrArea(value):
    return value

# Evaluates the quality of the material on the exterior
def ExterQual(value):
    return make_vector(np.array(['Ex','Gd','TA','Fa','Po',]), value)

# Evaluates the present condition of the material on the exterior
def ExterCond(value):
    return make_vector(np.array(['Ex','Gd','TA','Fa','Po',]), value)

# Type of foundation
def Foundation(value):
    return make_vector(np.array(['BrkTil','CBlock','PConc','Slab','Stone','Wood']), value)

# Evaluates the height of the basement        
def BsmtQual(value):
    return make_vector(np.array(['Ex','Gd','TA','Fa','Po','NA']), value)

# Evaluates the general condition of the basement
def BsmtCond(value):
    return make_vector(np.array(['Ex','Gd','TA','Fa','Po','NA']), value)

# Refers to walkout or garden level walls
def BsmtExposure(value):
    return make_vector(np.array(['Gd','Av','Mn','No','NA']), value)
# Rating of basement finished area
def BsmtFinType1(value):
    return make_vector(np.array(['GLQ','ALQ','BLQ','Rec','LwQ','Unf','NA']), value)

# Type 1 finished square feet
def BsmtFinSF1(value):
    return value

# Rating of basement finished area (if multiple types)
def BsmtFinType2(value):
    return make_vector(np.array(['GLQ','ALQ','BLQ','Rec','LwQ','Unf','NA']), value)

# Type 2 finished square feet
def BsmtFinSF2(value):
    return value

# Unfinished square feet of basement area
def BsmtUnfSF(value):
    return value

# Total square feet of basement area
def TotalBsmtSF(value):
    return value

def Heating(value):
    return make_vector(np.array(['Floor','GasA','GasW','Grav','OthW','Wall']), value)

def HeatingQC(value):
    return make_vector(np.array(['Ex','Gd','TA','Fa','Po']), value)

def CentralAir(value):
    if value == 'N':
        return np.array([0])
    elif value == 'Y':
        return np.array([1])
    else:
        return np.array([0])
        
def Electrical(value):
    return make_vector(np.array(['SBrkr','FuseA','FuseF','FuseP','Mix']), value)

def _1stFlrSF(value):
    return value
def _2ndFlrSF(value):
    return value
def LowQualFinSF(value):
    return value
def GrLivArea(value):
    return value
def BsmtFullBath(value):
    return value
def BsmtHalfBath(value):
    return value
def FullBath(value):
    return value
def HalfBath(value):
    return value
def Bedroom(value):
    return value
def Kitchen(value):
    return value
def KitchenQual(value):
    return make_vector(np.array(['Ex','Gd','TA','Fa','Po']), value)
def TotRmsAbvGrd(value):
    return value
def Functional(value):
    return make_vector(np.array(['Typ','Min1','Min2','Mod','Maj1','Maj2','Sev','Sal']), value)
def Fireplaces(value):
    return value
def FireplaceQu(value):
    return make_vector(np.array(['Ex','Gd','TA','Fa','Po','NA']), value)
def GarageType(value):
    return make_vector(np.array(['2Types','Attchd','Basment','BuiltIn','CarPort','Detchd','NA']), value)
def GarageYrBlt(value):
    return np.array([]) # dont know how to use yet
def GarageFinish(value):
    return make_vector(np.array(['Fin','RFn','Unf','NA']), value)
def GarageCars(value):
    return value
def GarageArea(value):
    return value
def GarageQual(value):
    return make_vector(np.array(['Ex','Gd','TA','Fa','Po','NA']), value)
def GarageCond(value):
    return make_vector(np.array(['Ex','Gd','TA','Fa','Po','NA']), value)
def PavedDrive(value):
    return make_vector(np.array(['Y','P','N']), value)
def WoodDeckSF(value):
    return value
def OpenPorchSF(value):
    return value
def EnclosedPorch(value):
    return value
def _3SsnPorch(value):
    return value
def ScreenPorch(value):
    return value
def PoolArea(value):
    return value
def PoolQC(value):
    return make_vector(np.array(['Ex','Gd','TA','Fa','NA']), value)
def Fence(value):
    return make_vector(np.array(['GdPrv','MnPrv','GdWo','MnWw','NA']), value)
def MiscFeature(value):
    return make_vector(np.array(['Elev','Gar2','Othr','Shed','TenC','NA']),value)
def MiscVal(value):
    return value
def MoSold(value):
    return np.array([]) # dont know how to use this yet
def YrSold(value):
    return np.array([]) # dont know how to use this yet
def SaleType(value):
    return make_vector(np.array(['WD','CWD','VWD','New','COD','Con','ConLw','ConLI','ConLD','Oth']), value)
def SaleCondition(value):
    return make_vector(np.array(['Normal','Abnorml','AdjLand','Alloca','Family','Partial']), value)

def preprocess_row_test(row):
    return np.hstack([
        Id(row[0]),
        MSSubClass(row[1]),
        MSZoning(row[2]),
        LotFrontage(row[3]),
        LotArea(row[4]),
        Street(row[5]),
        Alley(row[6]),
        LotShape(row[7]),
        LandContour(row[8]),
        Utilities(row[9]),
        LotConfig(row[10]),
        LandSlope(row[11]),
        Neighborhood(row[12]),
        Condition1(row[13]),
        Condition2(row[14]),
        BldgType(row[15]),
        HouseStyle(row[16]),
        OverallQual(row[17]),
        OverallCond(row[18]),
        YearBuilt(row[19]),
        YearRemodAdd(row[20]),
        RoofStyle(row[21]),
        RoofMatl(row[22]),
        Exterior1st(row[23]),
        Exterior2nd(row[24]),
        MasVnrType(row[25]),
        MasVnrArea(row[26]),
        ExterQual(row[27]),
        ExterCond(row[28]),
        Foundation(row[29]),
        BsmtQual(row[30]),
        BsmtCond(row[31]),
        BsmtExposure(row[32]),
        BsmtFinType1(row[33]),
        BsmtFinSF1(row[34]),
        BsmtFinType2(row[35]),
        BsmtFinSF2(row[36]),
        BsmtUnfSF(row[37]),
        TotalBsmtSF(row[38]),
        Heating(row[39]),
        HeatingQC(row[40]),
        CentralAir(row[41]),
        Electrical(row[42]),
        _1stFlrSF(row[43]),
        _2ndFlrSF(row[44]),
        LowQualFinSF(row[45]),
        GrLivArea(row[46]),
        BsmtFullBath(row[47]),
        BsmtHalfBath(row[48]),
        FullBath(row[49]),
        HalfBath(row[50]),
        Bedroom(row[51]),
        Kitchen(row[52]),
        KitchenQual(row[53]),
        TotRmsAbvGrd(row[54]),
        Functional(row[55]),
        Fireplaces(row[56]),
        FireplaceQu(row[57]),
        GarageType(row[58]),
        GarageYrBlt(row[59]),
        GarageFinish(row[60]),
        GarageCars(row[61]),
        GarageArea(row[62]),
        GarageQual(row[63]),
        GarageCond(row[64]),
        PavedDrive(row[65]),
        WoodDeckSF(row[66]),
        OpenPorchSF(row[67]),
        EnclosedPorch(row[68]),
        _3SsnPorch(row[69]),
        ScreenPorch(row[70]),
        PoolArea(row[71]),
        PoolQC(row[72]),
        Fence(row[73]),
        MiscFeature(row[74]),
        MiscVal(row[75]),
        MoSold(row[76]),
        YrSold(row[77]),
        SaleType(row[78]),
        SaleCondition(row[79])
    ])

def preprocess_row_train(row):
    return np.hstack((preprocess_row_test(row),row[80]))

def preprocess(input_file, output, train=True):
    df = pandas.read_csv(input_file, header=0)
    print("opened input file")
    if train:
        pp_rows = np.empty(shape=(1,331)) # this 330 could change, it depends on the functions
        for index, row in df.iterrows():
            pp_row = preprocess_row_train(row)
            pp_rows = np.vstack((pp_rows,pp_row))
    else:
        pp_rows = np.empty(shape=(1,330)) # this 330 could change, it depends on the functions
        for index, row in df.iterrows():
            pp_row = preprocess_row_test(row)
            pp_rows = np.vstack((pp_rows,pp_row))
    np.savetxt(output, pp_rows, delimiter=",")
preprocess('train.csv', 'preprocessed/train.csv', train=True)
preprocess('test.csv', 'preprocessed/test.csv', train=False)
