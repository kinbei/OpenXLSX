from typing import Any, List

from typing import overload

class XLCell:
    def __init__(self, *args, **kwargs) -> None: ...
    def cellReference(self, *args, **kwargs) -> Any: ...
    def formula(self) -> str: ...
    def hasFormula(self) -> bool: ...

    def setFormula(self, formula: str) -> None: ...

    def value(self, *args, **kwargs) -> Any: ...
    def valueType(self, *args, **kwargs) -> Any: ...

class XLCellRange:
    def __init__(self, *args, **kwargs) -> None: ...
    def clear(self) -> None: ...
    def numColumns(self) -> int: ...

    def numRows(self) -> int: ...

    def __iter__(self) -> iterator: ...


class XLCellReference.:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, cellAddress: str) -> None: ...

    @overload
    def __init__(self, row: int, column: int) -> None: ...

    @overload
    def __init__(self, row: int, column: str) -> None: ...

    @overload
    def __init__(*args, **kwargs) -> Any: ...

    def address(self) -> str: ...

    def column(self) -> int: ...

    def row(self) -> int: ...

    def setAddress(self, address: str) -> None: ...

    def setColumn(self, columnNumber: int) -> None: ...

    def setRow(self, rowNumber: int) -> None: ...

    def setRowAndColumn(self, row: int, column: int) -> None: ...

class XLCellValue:
    def __init__(self, *args, **kwargs) -> None: ...
    def asString(self) -> str: ...
    def clear(self) -> None: ...
    def valueType(self, *args, **kwargs) -> Any: ...
    @property
    def booleanValue(self) -> Any: ...
    @booleanValue.setter
    def booleanValue(self, val: Any) -> None: ...
    @property
    def floatValue(self) -> Any: ...
    @floatValue.setter
    def floatValue(self, val: Any) -> None: ...
    @property
    def integerValue(self) -> Any: ...
    @integerValue.setter
    def integerValue(self, val: Any) -> None: ...
    @property
    def stringValue(self) -> Any: ...
    @stringValue.setter
    def stringValue(self, val: Any) -> None: ...
    @property
    def value(self) -> Any: ...
    @value.setter
    def value(self, val: Any) -> None: ...

class XLChartsheet:
    def __init__(self, *args, **kwargs) -> None: ...

    def clone(self, newName: str) -> None: ...

    def color(self, *args, **kwargs) -> Any: ...

    def index(self) -> int: ...

    def isSelected(self) -> bool: ...

    def name(self) -> str: ...

    def setColor(self, color) -> None: ...

    def setIndex(self, index: int) -> None: ...

    def setName(self, name: str) -> None: ...

    def setSelected(self, selected: bool) -> None: ...

    def setVisibility(self, visibility) -> None: ...

    def visibility(self, *args, **kwargs) -> Any: ...

class XLColor:
    @overload
    def __init__(self) -> None: ...

    @overload
    def __init__(self, alpha: int, red: int, green: int, blue: int) -> None: ...

    @overload
    def __init__(self, red: int, green: int, blue: int) -> None: ...

    @overload
    def __init__(self, hexCode: str) -> None: ...

    @overload
    def __init__(*args, **kwargs) -> Any: ...
    @overload
    def blue(self) -> int: ...
    @overload
    def blue(self) -> str: ...
    @overload
    def blue(*args, **kwargs) -> Any: ...
    def green(self) -> int: ...
    @overload
    def red(self) -> int: ...
    @overload
    def red(self) -> int: ...

    @overload
    def red(*args, **kwargs) -> Any: ...

    @overload
    def set(self, alpha: int, red: int, green: int, blue: int) -> None: ...

    @overload
    def set(self, red: int, green: int, blue: int) -> None: ...

    @overload
    def set(self, hexCode: str) -> None: ...

    @overload
    def set(*args, **kwargs) -> Any: ...

class XLColumn:
    def __init__(self, *args, **kwargs) -> None: ...

    def isHidden(self) -> bool: ...

    def setHidden(self, state: bool) -> None: ...

    def setWidth(self, width: float) -> None: ...

    def width(self) -> float: ...

class XLDocument:
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, filename: str) -> None: ...
    @overload
    def __init__(*args, **kwargs) -> Any: ...
    def close(self) -> None: ...
    def create(self, filename: str) -> None: ...
    def deleteProperty(self, property) -> None: ...
    def name(self) -> str: ...
    def open(self, filename: str) -> None: ...
    def path(self) -> str: ...
    def property(self, property) -> str: ...
    def save(self) -> None: ...
    def saveAs(self, filename: str) -> None: ...
    def setProperty(self, property, value: str) -> None: ...
    def workbook(self, *args, **kwargs) -> Any: ...

class XLProperty:
    AppVersion: Any = ...
    Application: Any = ...
    Category: Any = ...
    Company: Any = ...
    CreationDate: Any = ...
    Creator: Any = ...
    Description: Any = ...
    DocSecurity: Any = ...
    HyperlinkBase: Any = ...
    HyperlinksChanged: Any = ...
    Keywords: Any = ...
    LastModifiedBy: Any = ...
    LastPrinted: Any = ...
    LinksUpToDate: Any = ...
    Manager: Any = ...
    ModificationDate: Any = ...
    ScaleCrop: Any = ...
    SharedDoc: Any = ...
    Subject: Any = ...
    Title: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __getstate__(self) -> Any: ...
    def __hash__(self) -> Any: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other) -> Any: ...
    def __setstate__(self, state) -> Any: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class XLRow:
    def __init__(self, *args, **kwargs) -> None: ...

    def cellCount(self) -> int: ...

    def descent(self) -> float: ...

    def height(self) -> float: ...

    def isHidden(self) -> bool: ...

    def rowNumber(self) -> int: ...

    def setDescent(self, descent: float) -> None: ...

    def setHeight(self, height: float) -> None: ...

    def setHidden(self, state: bool) -> None: ...

class XLSheet:
    def __init__(self, *args, **kwargs) -> None: ...

    def chartsheet(self) -> XLChartsheet: ...

    def clone(self, newName: str) -> None: ...

    def color(self) -> XLColor: ...

    def getType(self, *args, **kwargs) -> Any: ...

    def index(self) -> int: ...

    def name(self) -> str: ...

    def setColor(self, color: XLColor) -> None: ...

    def setIndex(self, index: int) -> None: ...

    def setName(self, name: str) -> None: ...

    def setSelected(self, selected: bool) -> None: ...

    def setVisibility(self, visibility) -> None: ...

    def visibility(self, *args, **kwargs) -> Any: ...

    def worksheet(self, *args, **kwargs) -> Any: ...

class XLSheetState:
    Hidden: Any = ...
    VeryHidden: Any = ...
    Visible: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __getstate__(self) -> Any: ...
    def __hash__(self) -> Any: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other) -> Any: ...
    def __setstate__(self, state) -> Any: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class XLSheetType:
    Chartsheet: Any = ...
    Dialogsheet: Any = ...
    Macrosheet: Any = ...
    Worksheet: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __getstate__(self) -> Any: ...
    def __hash__(self) -> Any: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other) -> Any: ...
    def __setstate__(self, state) -> Any: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class XLValueType:
    Boolean: Any = ...
    Empty: Any = ...
    Error: Any = ...
    Float: Any = ...
    Integer: Any = ...
    String: Any = ...
    __entries: Any = ...
    def __init__(self, arg0: int) -> None: ...
    def __eq__(self, other) -> Any: ...
    def __getstate__(self) -> Any: ...
    def __hash__(self) -> Any: ...
    def __index__(self) -> int: ...
    def __int__(self) -> int: ...
    def __ne__(self, other) -> Any: ...
    def __setstate__(self, state) -> Any: ...
    @property
    def name(self) -> Any: ...
    @property
    def __doc__(self) -> Any: ...
    @property
    def __members__(self) -> Any: ...

class XLWorkbook:
    def __init__(self, *args, **kwargs) -> None: ...

    def addWorksheet(self, name: str) -> None: ...

    def chartsheet(self, name: str) -> XLChartsheet: ...

    def chartsheetCount(self) -> int: ...

    def chartsheetExists(self, name: str) -> bool: ...

    def chartsheetNames(self) -> List[str]: ...

    def cloneSheet(self, existingName: str, newName: str) -> None: ...

    def deleteNamedRanges(self) -> None: ...

    def deleteSheet(self, name: str) -> None: ...

    def indexOfSheet(self, name: str) -> int: ...

    def setSheetIndex(self, name: str, index: int) -> None: ...

    @overload
    def sheet(self, index: int) -> XLSheet: ...

    @overload
    def sheet(self, name: str) -> XLSheet: ...

    @overload
    def sheet(*args, **kwargs) -> Any: ...

    def sheetCount(self) -> int: ...

    def sheetExists(self, name: str) -> bool: ...

    def sheetNames(self) -> List[str]: ...

    @overload
    def typeOfSheet(self, index: int) -> XLSheetType: ...

    @overload
    def typeOfSheet(self, name: str) -> XLSheetType: ...

    @overload
    def typeOfSheet(*args, **kwargs) -> Any: ...
    def worksheet(self, *args, **kwargs) -> Any: ...

    def worksheetCount(self) -> int: ...

    def worksheetExists(self, name: str) -> bool: ...

    def worksheetNames(self) -> List[str]: ...

class XLWorksheet:
    def __init__(self, *args, **kwargs) -> None: ...

    @overload
    def cell(self, address: str) -> XLCell: ...

    @overload
    def cell(self, reference) -> XLCell: ...

    @overload
    def cell(self, row: int, column: int) -> XLCell: ...

    @overload
    def cell(*args, **kwargs) -> Any: ...

    def clone(self, newName: str) -> None: ...

    def color(self) -> XLColor: ...

    def column(self, columnNumber: int) -> XLColumn: ...

    def columnCount(self) -> int: ...

    def index(self) -> int: ...

    def isSelected(self) -> bool: ...

    def name(self) -> str: ...

    @overload
    def range(self) -> XLCellRange: ...

    @overload
    def range(self, topLeft, bottomRight) -> XLCellRange: ...

    @overload
    def range(*args, **kwargs) -> Any: ...

    def row(self, rowNumber: int) -> XLRow: ...

    def rowCount(self) -> int: ...

    def setColor(self, color: XLColor) -> None: ...

    def setIndex(self, index: int) -> None: ...

    def setName(self, name: str) -> None: ...

    def setSelected(self, selected: bool) -> None: ...

    def setVisibility(self, visibility: XLSheetState) -> None: ...

    def visibility(self) -> XLSheetState: ...
