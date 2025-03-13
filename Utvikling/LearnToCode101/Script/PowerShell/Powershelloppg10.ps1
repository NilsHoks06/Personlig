#Beregn diskplass brukt av PDF filer i alle mapper på C:\

$folderPath = "C:\"
$pdfFiles = Get-ChildItem -Path $folderPath -Recurse -Filter "*.pdf" -File
$totalSize = 0

foreach ($pdfFile in $pdfFiles) {
    $totalSize += $pdfFile.Length
}

# Konverter størrelse til MB
$totalSizeMB = [math]::round($totalSize / 1MB, 2)

Write-Output "Total diskplass brukt av PDF-filer: $totalSizeMB MB"
