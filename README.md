# affordability-model

## UI

- UI_YR
- UI_%DIC 
- UI_FS 
- UI_ST
- UI_%DIS
- UI_YRS_SAVING
- UI_%I
- UI_IT
- UI_LS
- UI_HRW
- UI_UNIV

## Plots

Funds from family income
--------------------------

#### UI

- UI_YR
- UI_%DIC 
- UI_FS 
- UI_ST

#### Query

- `Q_PG = Q( UI_YR, PGModel )`

- `Q_MFI = Q( UI_YR, UI_ST, MFIModel )`

#### Functions

- `FI = [Lim (0 -> 200) %MFI * Q_MFI ] / 100`

- `BN = Q_PG.F + ((UI_FS - 1) * Q_PG.A)`

- `DI = FI - BN`

#### Plot

- `FFI = (UI_%DIC * DI) / 100`

Savings for College
-------------------

#### UI

- UI_YR
- UI_ST
- UI_FS
- UI_%DIS
- UI_YRS_SAVING
- UI_%I

#### Query

- `Q_PG = Q( UI_YR, PGModel )`

- `Q_MFI = Q( UI_YR, UI_ST, MFIModel )`


#### Functions 

- `FI = [Lim (0 -> 200) %MFI * Q_MFI ] / 100`

- `BN = Q_PG.F + ((UI_FS - 1) * Q_PG.A)`

- `DI = FI - BN`

- `ContributionToSavings = UI_%DIS * DI / 100`

- `InterestComputation = (A/12) * [ (1 + i/12) ^ ( n * 12 )  - 1 ] / (i/12)`

#### Plot

- `CS = InterestComputation( ContributionToSavings, UI_%I, UI_YRS_SAVING )`


State Need Grant Washington
----------------------------

#### UI

- UI_YR
- UI_IT

#### Query

- `Q_MG = Q(UI_YR, UI_IT, StateNeedGrantModel)`

- `Q_%MG = FILTER( DB(UI_YR, StateNeedGrantDistroScheduleModel), [lim 0->200]%MFI )`

#### Functions

- `GRANT = Q_MG * Q_%MG / 100`

Pell Grant
----------

#### UI

- UI_YR
- UI_IT
- UI_ST
- UI_LS

#### Query
- `Q_MFI = Q( UI_YR, UI_ST, MFIModel )`

- `Q_EFC = Q( FI, ExpectedFamilyContributionModel )`

- `Q_TUT = Q(UI_YR, UI_IT, UI_ST, TutionModel)`

- `Q_LE = Q(UI_YR, UI_ST, UI_LS, UI_IT, LivingExpensesModel)`

#### Functions

- `COA = Q_TUT + Q_LE`

- `FI = [Lim (0 -> 200) %MFI * Q_MFI ] / 100`

#### Plot

- `AWARD = Q( Filter1 && Filter2 && Filter3, PellGrantModel)`
     - `Filter1 = ( lowerEFC <= Q_EFC <= upperEFC )`
     - `Filter2 = ( lowerCOA <= COA <= upperCOA )` 
     - `Filter3 = ( UI_YR )`

Funds from Work
--------------

#### UI

- UI_YR
- UI_HRW

#### Query

- `MW = Q( UI_YR, UI_ST, MinimumWageModel)`

#### Functions

- `YI = UI_HRW * MW`


State Appropriation
-------------------

#### UI

- UI_YR
- UI_ST
- UI_IT

#### Query

- `Q_IN[] = Q( UI_IT, UI_ST, InstitutionModel)`
- `Q_TAPPR = Q(UI_YR, Q_IN[], AppropriationModel)`
- `Q_ENNR = Q(UI_YR, Q_IN[], EnrollmentModel)`


#### Function

- `APPR/STU = Q_TAPPR / Q_ENNR` 

#### Plot

- `APPR/STU`



Student Aid
------------------

#### UI

- UI_YR
- UI_ST
- UI_IT


#### Query

- `Q_SAID = Q( UI_YR, UI_ST, UI_IT, [Lim (0 -> 200) %MFI], StudentAidModel)`

Enrollment
----------

#### UI

- UI_YR
- UI_ST
- UI_IT
- UI_UNIV

#### Query

- `EN = AGGR( Q( UI_YR, UI_ST, UI_IT, UI_UNIV, EnrollmentModel) )`


## Legend

Refer spreadsheet for abbreviations [link](https://docs.google.com/a/uw.edu/spreadsheets/d/1QxwDoSTouTrQyf1P_X0LqK6ULsh6QGpIv9a_rld4seo/edit?usp=sharing)