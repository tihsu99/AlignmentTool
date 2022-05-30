import FWCore.ParameterSet.Config as cms

from AlignmentTool.ESAlignTool.DefaultMatrixElementIter_cfi import * #DefaultMatrixElement_Iter 
MatrixElementsTmp = DefaultMatrixElementIter.clone()

########## Modify the Matrix element for each iterator ################
#  MatrixElementsTmp.Iter1_ESpFdX = cms.double(0.2)
#  MatrixElementsTmp.Iter2_ESpFdX = cms.double(0.1)

MatrixElementsTmp.Iter1_ESpFdX = cms.double(0.0165087)
MatrixElementsTmp.Iter1_ESpFdY = cms.double(-0.0330137)
MatrixElementsTmp.Iter1_ESpFdZ = cms.double(0.0199365)
MatrixElementsTmp.Iter1_ESpFdAlpha = cms.double(-0.00118326)
MatrixElementsTmp.Iter1_ESpFdBeta = cms.double(-0.000258415)
MatrixElementsTmp.Iter1_ESpFdGamma = cms.double(-0.000592389)
MatrixElementsTmp.Iter1_ESpRdX = cms.double(0.0325249)
MatrixElementsTmp.Iter1_ESpRdY = cms.double(-0.0428778)
MatrixElementsTmp.Iter1_ESpRdZ = cms.double(-0.0422103)
MatrixElementsTmp.Iter1_ESpRdAlpha = cms.double(0.00048293)
MatrixElementsTmp.Iter1_ESpRdBeta = cms.double(0.00079666)
MatrixElementsTmp.Iter1_ESpRdGamma = cms.double(-0.000618615)
MatrixElementsTmp.Iter1_ESmFdX = cms.double(-0.177417)
MatrixElementsTmp.Iter1_ESmFdY = cms.double(0.0136839)
MatrixElementsTmp.Iter1_ESmFdZ = cms.double(0.0336363)
MatrixElementsTmp.Iter1_ESmFdAlpha = cms.double(-0.000642722)
MatrixElementsTmp.Iter1_ESmFdBeta = cms.double(-0.000299349)
MatrixElementsTmp.Iter1_ESmFdGamma = cms.double(0.000373536)
MatrixElementsTmp.Iter1_ESmRdX = cms.double(-0.130578)
MatrixElementsTmp.Iter1_ESmRdY = cms.double(0.117807)
MatrixElementsTmp.Iter1_ESmRdZ = cms.double(-0.00852279)
MatrixElementsTmp.Iter1_ESmRdAlpha = cms.double(-0.00110086)
MatrixElementsTmp.Iter1_ESmRdBeta = cms.double(-0.000414439)
MatrixElementsTmp.Iter1_ESmRdGamma = cms.double(0.000361889)

MatrixElementsTmp.Iter2_ESpFdX = cms.double(-0.000847115)
MatrixElementsTmp.Iter2_ESpFdY = cms.double(6.03036e-06)
MatrixElementsTmp.Iter2_ESpFdZ = cms.double(-0.00254687)
MatrixElementsTmp.Iter2_ESpFdAlpha = cms.double(0.000136065)
MatrixElementsTmp.Iter2_ESpFdBeta = cms.double(7.76542e-05)
MatrixElementsTmp.Iter2_ESpFdGamma = cms.double(5.47079e-06)
MatrixElementsTmp.Iter2_ESpRdX = cms.double(0.0317123)
MatrixElementsTmp.Iter2_ESpRdY = cms.double(7.63477e-05)
MatrixElementsTmp.Iter2_ESpRdZ = cms.double(0.0114546)
MatrixElementsTmp.Iter2_ESpRdAlpha = cms.double(0.000217211)
MatrixElementsTmp.Iter2_ESpRdBeta = cms.double(-0.000188524)
MatrixElementsTmp.Iter2_ESpRdGamma = cms.double(-3.57454e-05)
MatrixElementsTmp.Iter2_ESmFdX = cms.double(-0.0121663)
MatrixElementsTmp.Iter2_ESmFdY = cms.double(0.0259373)
MatrixElementsTmp.Iter2_ESmFdZ = cms.double(0.0337089)
MatrixElementsTmp.Iter2_ESmFdAlpha = cms.double(-0.000158682)
MatrixElementsTmp.Iter2_ESmFdBeta = cms.double(-0.000353395)
MatrixElementsTmp.Iter2_ESmFdGamma = cms.double(-1.44937e-06)
MatrixElementsTmp.Iter2_ESmRdX = cms.double(-0.0652887)
MatrixElementsTmp.Iter2_ESmRdY = cms.double(-0.000152135)
MatrixElementsTmp.Iter2_ESmRdZ = cms.double(-0.0157538)
MatrixElementsTmp.Iter2_ESmRdAlpha = cms.double(0.000724109)
MatrixElementsTmp.Iter2_ESmRdBeta = cms.double(-7.75224e-05)
MatrixElementsTmp.Iter2_ESmRdGamma = cms.double(2.50324e-05)

MatrixElementsTmp.Iter3_ESpFdX = cms.double(0.000282205)
MatrixElementsTmp.Iter3_ESpFdY = cms.double(-0.0094965)
MatrixElementsTmp.Iter3_ESpFdZ = cms.double(0.00236046)
MatrixElementsTmp.Iter3_ESpFdAlpha = cms.double(2.94951e-05)
MatrixElementsTmp.Iter3_ESpFdBeta = cms.double(-6.18775e-05)
MatrixElementsTmp.Iter3_ESpFdGamma = cms.double(9.49333e-06)
MatrixElementsTmp.Iter3_ESpRdX = cms.double(0.0292326)
MatrixElementsTmp.Iter3_ESpRdY = cms.double(6.79337e-05)
MatrixElementsTmp.Iter3_ESpRdZ = cms.double(0.0191075)
MatrixElementsTmp.Iter3_ESpRdAlpha = cms.double(0.000203878)
MatrixElementsTmp.Iter3_ESpRdBeta = cms.double(-0.000649609)
MatrixElementsTmp.Iter3_ESpRdGamma = cms.double(-5.39694e-05)
MatrixElementsTmp.Iter3_ESmFdX = cms.double(0.00364376)
MatrixElementsTmp.Iter3_ESmFdY = cms.double(0.00160501)
MatrixElementsTmp.Iter3_ESmFdZ = cms.double(0.00601993)
MatrixElementsTmp.Iter3_ESmFdAlpha = cms.double(-0.000205284)
MatrixElementsTmp.Iter3_ESmFdBeta = cms.double(6.55336e-05)
MatrixElementsTmp.Iter3_ESmFdGamma = cms.double(-5.78801e-05)
MatrixElementsTmp.Iter3_ESmRdX = cms.double(-0.0451792)
MatrixElementsTmp.Iter3_ESmRdY = cms.double(0.000500557)
MatrixElementsTmp.Iter3_ESmRdZ = cms.double(0.00490403)
MatrixElementsTmp.Iter3_ESmRdAlpha = cms.double(6.79993e-05)
MatrixElementsTmp.Iter3_ESmRdBeta = cms.double(4.21553e-05)
MatrixElementsTmp.Iter3_ESmRdGamma = cms.double(-6.26814e-06)

MatrixElementsTmp.Iter4_ESpFdX = cms.double(-0.000445626)
MatrixElementsTmp.Iter4_ESpFdY = cms.double(0.00230811)
MatrixElementsTmp.Iter4_ESpFdZ = cms.double(0.000414281)
MatrixElementsTmp.Iter4_ESpFdAlpha = cms.double(1.25165e-05)
MatrixElementsTmp.Iter4_ESpFdBeta = cms.double(4.32458e-05)
MatrixElementsTmp.Iter4_ESpFdGamma = cms.double(3.34932e-06)
MatrixElementsTmp.Iter4_ESpRdX = cms.double(0.0151832)
MatrixElementsTmp.Iter4_ESpRdY = cms.double(-0.00053119)
MatrixElementsTmp.Iter4_ESpRdZ = cms.double(-0.00119045)
MatrixElementsTmp.Iter4_ESpRdAlpha = cms.double(-6.13234e-06)
MatrixElementsTmp.Iter4_ESpRdBeta = cms.double(2.30481e-05)
MatrixElementsTmp.Iter4_ESpRdGamma = cms.double(1.86674e-06)
MatrixElementsTmp.Iter4_ESmFdX = cms.double(8.02848e-05)
MatrixElementsTmp.Iter4_ESmFdY = cms.double(0.00701603)
MatrixElementsTmp.Iter4_ESmFdZ = cms.double(-0.00140006)
MatrixElementsTmp.Iter4_ESmFdAlpha = cms.double(-1.12666e-05)
MatrixElementsTmp.Iter4_ESmFdBeta = cms.double(1.2243e-05)
MatrixElementsTmp.Iter4_ESmFdGamma = cms.double(5.7311e-07)
MatrixElementsTmp.Iter4_ESmRdX = cms.double(-0.0434965)
MatrixElementsTmp.Iter4_ESmRdY = cms.double(0.00115824)
MatrixElementsTmp.Iter4_ESmRdZ = cms.double(-0.00239272)
MatrixElementsTmp.Iter4_ESmRdAlpha = cms.double(-4.99348e-05)
MatrixElementsTmp.Iter4_ESmRdBeta = cms.double(-0.000107615)
MatrixElementsTmp.Iter4_ESmRdGamma = cms.double(-9.50123e-07)

MatrixElementsTmp.Iter5_ESpFdX = cms.double(-0.00018321)
MatrixElementsTmp.Iter5_ESpFdY = cms.double(-0.00712469)
MatrixElementsTmp.Iter5_ESpFdZ = cms.double(0.000404392)
MatrixElementsTmp.Iter5_ESpFdAlpha = cms.double(1.10585e-05)
MatrixElementsTmp.Iter5_ESpFdBeta = cms.double(1.71438e-05)
MatrixElementsTmp.Iter5_ESpFdGamma = cms.double(3.72891e-06)
MatrixElementsTmp.Iter5_ESpRdX = cms.double(0.0125718)
MatrixElementsTmp.Iter5_ESpRdY = cms.double(-0.000203028)
MatrixElementsTmp.Iter5_ESpRdZ = cms.double(0.000961246)
MatrixElementsTmp.Iter5_ESpRdAlpha = cms.double(-3.08558e-05)
MatrixElementsTmp.Iter5_ESpRdBeta = cms.double(-1.13952e-05)
MatrixElementsTmp.Iter5_ESpRdGamma = cms.double(-3.04507e-07)
MatrixElementsTmp.Iter5_ESmFdX = cms.double(-0.000248477)
MatrixElementsTmp.Iter5_ESmFdY = cms.double(-0.00318653)
MatrixElementsTmp.Iter5_ESmFdZ = cms.double(0.00466569)
MatrixElementsTmp.Iter5_ESmFdAlpha = cms.double(-7.46412e-05)
MatrixElementsTmp.Iter5_ESmFdBeta = cms.double(5.13924e-05)
MatrixElementsTmp.Iter5_ESmFdGamma = cms.double(-3.02389e-06)
MatrixElementsTmp.Iter5_ESmRdX = cms.double(-0.0174922)
MatrixElementsTmp.Iter5_ESmRdY = cms.double(0.00265431)
MatrixElementsTmp.Iter5_ESmRdZ = cms.double(-0.00377073)
MatrixElementsTmp.Iter5_ESmRdAlpha = cms.double(-3.17123e-05)
MatrixElementsTmp.Iter5_ESmRdBeta = cms.double(-0.000157136)
MatrixElementsTmp.Iter5_ESmRdGamma = cms.double(-3.25851e-05)

MatrixElementsTmp.Iter6_ESpFdX = cms.double(-6.9365e-06)
MatrixElementsTmp.Iter6_ESpFdY = cms.double(4.30612e-06)
MatrixElementsTmp.Iter6_ESpFdZ = cms.double(0.000262023)
MatrixElementsTmp.Iter6_ESpFdAlpha = cms.double(4.82685e-07)
MatrixElementsTmp.Iter6_ESpFdBeta = cms.double(1.40494e-06)
MatrixElementsTmp.Iter6_ESpFdGamma = cms.double(4.37655e-08)
MatrixElementsTmp.Iter6_ESpRdX = cms.double(-1.83389e-05)
MatrixElementsTmp.Iter6_ESpRdY = cms.double(5.72239e-06)
MatrixElementsTmp.Iter6_ESpRdZ = cms.double(-5.44351e-05)
MatrixElementsTmp.Iter6_ESpRdAlpha = cms.double(-1.98729e-07)
MatrixElementsTmp.Iter6_ESpRdBeta = cms.double(1.55808e-06)
MatrixElementsTmp.Iter6_ESpRdGamma = cms.double(8.26144e-09)
MatrixElementsTmp.Iter6_ESmFdX = cms.double(-0.000206539)
MatrixElementsTmp.Iter6_ESmFdY = cms.double(-0.00281017)
MatrixElementsTmp.Iter6_ESmFdZ = cms.double(-0.000141244)
MatrixElementsTmp.Iter6_ESmFdAlpha = cms.double(-1.77742e-06)
MatrixElementsTmp.Iter6_ESmFdBeta = cms.double(-1.31986e-05)
MatrixElementsTmp.Iter6_ESmFdGamma = cms.double(-1.4383e-06)
MatrixElementsTmp.Iter6_ESmRdX = cms.double(-0.00412247)
MatrixElementsTmp.Iter6_ESmRdY = cms.double(-0.000139785)
MatrixElementsTmp.Iter6_ESmRdZ = cms.double(-0.00345045)
MatrixElementsTmp.Iter6_ESmRdAlpha = cms.double(6.01398e-05)
MatrixElementsTmp.Iter6_ESmRdBeta = cms.double(-2.06944e-05)
MatrixElementsTmp.Iter6_ESmRdGamma = cms.double(-1.71366e-06)

MatrixElementsTmp.Iter7_ESpFdX = cms.double(-1.67646e-05)
MatrixElementsTmp.Iter7_ESpFdY = cms.double(7.64117e-07)
MatrixElementsTmp.Iter7_ESpFdZ = cms.double(-7.74975e-06)
MatrixElementsTmp.Iter7_ESpFdAlpha = cms.double(4.82076e-08)
MatrixElementsTmp.Iter7_ESpFdBeta = cms.double(1.64074e-06)
MatrixElementsTmp.Iter7_ESpFdGamma = cms.double(-1.17913e-08)
MatrixElementsTmp.Iter7_ESpRdX = cms.double(7.694e-07)
MatrixElementsTmp.Iter7_ESpRdY = cms.double(3.45583e-08)
MatrixElementsTmp.Iter7_ESpRdZ = cms.double(-1.57288e-05)
MatrixElementsTmp.Iter7_ESpRdAlpha = cms.double(-6.77013e-09)
MatrixElementsTmp.Iter7_ESpRdBeta = cms.double(-5.69486e-08)
MatrixElementsTmp.Iter7_ESpRdGamma = cms.double(1.72368e-09)
MatrixElementsTmp.Iter7_ESmFdX = cms.double(-0.000686828)
MatrixElementsTmp.Iter7_ESmFdY = cms.double(-0.0012965)
MatrixElementsTmp.Iter7_ESmFdZ = cms.double(-0.00120776)
MatrixElementsTmp.Iter7_ESmFdAlpha = cms.double(3.24126e-05)
MatrixElementsTmp.Iter7_ESmFdBeta = cms.double(-2.98759e-05)
MatrixElementsTmp.Iter7_ESmFdGamma = cms.double(-7.25027e-06)
MatrixElementsTmp.Iter7_ESmRdX = cms.double(-0.00426184)
MatrixElementsTmp.Iter7_ESmRdY = cms.double(0.000372047)
MatrixElementsTmp.Iter7_ESmRdZ = cms.double(0.00549578)
MatrixElementsTmp.Iter7_ESmRdAlpha = cms.double(-0.000103799)
MatrixElementsTmp.Iter7_ESmRdBeta = cms.double(-3.81863e-05)
MatrixElementsTmp.Iter7_ESmRdGamma = cms.double(-2.92067e-06)

MatrixElementsTmp.Iter8_ESpFdX = cms.double(1.10862e-06)
MatrixElementsTmp.Iter8_ESpFdY = cms.double(5.03276e-07)
MatrixElementsTmp.Iter8_ESpFdZ = cms.double(1.87442e-05)
MatrixElementsTmp.Iter8_ESpFdAlpha = cms.double(5.07553e-08)
MatrixElementsTmp.Iter8_ESpFdBeta = cms.double(-9.41181e-08)
MatrixElementsTmp.Iter8_ESpFdGamma = cms.double(3.7656e-09)
MatrixElementsTmp.Iter8_ESpRdX = cms.double(4.59389e-07)
MatrixElementsTmp.Iter8_ESpRdY = cms.double(4.95359e-08)
MatrixElementsTmp.Iter8_ESpRdZ = cms.double(1.56472e-05)
MatrixElementsTmp.Iter8_ESpRdAlpha = cms.double(1.09575e-08)
MatrixElementsTmp.Iter8_ESpRdBeta = cms.double(-4.70679e-08)
MatrixElementsTmp.Iter8_ESpRdGamma = cms.double(-1.4304e-09)
MatrixElementsTmp.Iter8_ESmFdX = cms.double(1.34032e-05)
MatrixElementsTmp.Iter8_ESmFdY = cms.double(-2.23763e-06)
MatrixElementsTmp.Iter8_ESmFdZ = cms.double(0.000110834)
MatrixElementsTmp.Iter8_ESmFdAlpha = cms.double(6.16235e-08)
MatrixElementsTmp.Iter8_ESmFdBeta = cms.double(1.3597e-06)
MatrixElementsTmp.Iter8_ESmFdGamma = cms.double(4.37669e-08)
MatrixElementsTmp.Iter8_ESmRdX = cms.double(-2.52487e-05)
MatrixElementsTmp.Iter8_ESmRdY = cms.double(-3.61193e-06)
MatrixElementsTmp.Iter8_ESmRdZ = cms.double(6.03924e-05)
MatrixElementsTmp.Iter8_ESmRdAlpha = cms.double(3.80181e-07)
MatrixElementsTmp.Iter8_ESmRdBeta = cms.double(-2.49793e-06)
MatrixElementsTmp.Iter8_ESmRdGamma = cms.double(6.69186e-08)

MatrixElementsTmp.Iter9_ESpFdX = cms.double(-2.85184e-08)
MatrixElementsTmp.Iter9_ESpFdY = cms.double(-2.08052e-07)
MatrixElementsTmp.Iter9_ESpFdZ = cms.double(1.70061e-05)
MatrixElementsTmp.Iter9_ESpFdAlpha = cms.double(-1.32572e-08)
MatrixElementsTmp.Iter9_ESpFdBeta = cms.double(-3.99822e-09)
MatrixElementsTmp.Iter9_ESpFdGamma = cms.double(9.911e-10)
MatrixElementsTmp.Iter9_ESpRdX = cms.double(-4.16393e-07)
MatrixElementsTmp.Iter9_ESpRdY = cms.double(-1.47273e-07)
MatrixElementsTmp.Iter9_ESpRdZ = cms.double(-1.59776e-05)
MatrixElementsTmp.Iter9_ESpRdAlpha = cms.double(-1.10536e-08)
MatrixElementsTmp.Iter9_ESpRdBeta = cms.double(5.66705e-08)
MatrixElementsTmp.Iter9_ESpRdGamma = cms.double(1.22693e-09)
MatrixElementsTmp.Iter9_ESmFdX = cms.double(-1.21468e-06)
MatrixElementsTmp.Iter9_ESmFdY = cms.double(2.16698e-07)
MatrixElementsTmp.Iter9_ESmFdZ = cms.double(-1.52974e-05)
MatrixElementsTmp.Iter9_ESmFdAlpha = cms.double(-8.02736e-09)
MatrixElementsTmp.Iter9_ESmFdBeta = cms.double(-1.30448e-07)
MatrixElementsTmp.Iter9_ESmFdGamma = cms.double(-1.19083e-09)
MatrixElementsTmp.Iter9_ESmRdX = cms.double(-4.67063e-07)
MatrixElementsTmp.Iter9_ESmRdY = cms.double(-5.81607e-08)
MatrixElementsTmp.Iter9_ESmRdZ = cms.double(2.382e-06)
MatrixElementsTmp.Iter9_ESmRdAlpha = cms.double(2.59954e-09)
MatrixElementsTmp.Iter9_ESmRdBeta = cms.double(-4.23083e-08)
MatrixElementsTmp.Iter9_ESmRdGamma = cms.double(5.58833e-09)

MatrixElementsTmp.Iter10_ESpFdX = cms.double(-2.10742e-06)
MatrixElementsTmp.Iter10_ESpFdY = cms.double(2.25995e-07)
MatrixElementsTmp.Iter10_ESpFdZ = cms.double(-1.56512e-05)
MatrixElementsTmp.Iter10_ESpFdAlpha = cms.double(9.75014e-09)
MatrixElementsTmp.Iter10_ESpFdBeta = cms.double(2.04014e-07)
MatrixElementsTmp.Iter10_ESpFdGamma = cms.double(-3.09166e-09)
MatrixElementsTmp.Iter10_ESpRdX = cms.double(4.50778e-07)
MatrixElementsTmp.Iter10_ESpRdY = cms.double(1.53428e-07)
MatrixElementsTmp.Iter10_ESpRdZ = cms.double(1.56798e-05)
MatrixElementsTmp.Iter10_ESpRdAlpha = cms.double(1.04817e-08)
MatrixElementsTmp.Iter10_ESpRdBeta = cms.double(-5.47925e-08)
MatrixElementsTmp.Iter10_ESpRdGamma = cms.double(-1.29847e-09)
MatrixElementsTmp.Iter10_ESmFdX = cms.double(2.50526e-07)
MatrixElementsTmp.Iter10_ESmFdY = cms.double(-1.29997e-07)
MatrixElementsTmp.Iter10_ESmFdZ = cms.double(1.52605e-05)
MatrixElementsTmp.Iter10_ESmFdAlpha = cms.double(5.57373e-09)
MatrixElementsTmp.Iter10_ESmFdBeta = cms.double(2.92077e-08)
MatrixElementsTmp.Iter10_ESmFdGamma = cms.double(-4.16334e-10)
MatrixElementsTmp.Iter10_ESmRdX = cms.double(5.82758e-08)
MatrixElementsTmp.Iter10_ESmRdY = cms.double(-2.19424e-09)
MatrixElementsTmp.Iter10_ESmRdZ = cms.double(2.43268e-06)
MatrixElementsTmp.Iter10_ESmRdAlpha = cms.double(-2.46733e-09)
MatrixElementsTmp.Iter10_ESmRdBeta = cms.double(-4.74384e-10)
MatrixElementsTmp.Iter10_ESmRdGamma = cms.double(-8.12047e-10)

MatrixElementsTmp.Iter11_ESpFdX = cms.double(2.10449e-06)
MatrixElementsTmp.Iter11_ESpFdY = cms.double(3.88692e-08)
MatrixElementsTmp.Iter11_ESpFdZ = cms.double(2.02405e-05)
MatrixElementsTmp.Iter11_ESpFdAlpha = cms.double(3.34063e-10)
MatrixElementsTmp.Iter11_ESpFdBeta = cms.double(-2.10081e-07)
MatrixElementsTmp.Iter11_ESpFdGamma = cms.double(3.13084e-09)
MatrixElementsTmp.Iter11_ESpRdX = cms.double(-4.63726e-07)
MatrixElementsTmp.Iter11_ESpRdY = cms.double(-1.52889e-07)
MatrixElementsTmp.Iter11_ESpRdZ = cms.double(-1.59794e-05)
MatrixElementsTmp.Iter11_ESpRdAlpha = cms.double(-1.04712e-08)
MatrixElementsTmp.Iter11_ESpRdBeta = cms.double(5.37528e-08)
MatrixElementsTmp.Iter11_ESpRdGamma = cms.double(1.23641e-09)
MatrixElementsTmp.Iter11_ESmFdX = cms.double(-2.9941e-07)
MatrixElementsTmp.Iter11_ESmFdY = cms.double(1.75511e-07)
MatrixElementsTmp.Iter11_ESmFdZ = cms.double(-1.61352e-05)
MatrixElementsTmp.Iter11_ESmFdAlpha = cms.double(-9.09263e-09)
MatrixElementsTmp.Iter11_ESmFdBeta = cms.double(-2.61638e-08)
MatrixElementsTmp.Iter11_ESmFdGamma = cms.double(7.18557e-10)
MatrixElementsTmp.Iter11_ESmRdX = cms.double(2.11249e-08)
MatrixElementsTmp.Iter11_ESmRdY = cms.double(6.10946e-10)
MatrixElementsTmp.Iter11_ESmRdZ = cms.double(2.42336e-06)
MatrixElementsTmp.Iter11_ESmRdAlpha = cms.double(-1.95469e-09)
MatrixElementsTmp.Iter11_ESmRdBeta = cms.double(3.44128e-10)
MatrixElementsTmp.Iter11_ESmRdGamma = cms.double(5.60691e-11)

