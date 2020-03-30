{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "csvpath = os.path.join(\"..\",\"Resources\",\"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(csvpath,'r',newline='') as b_file:\n",
    "    csvreader = csv.reader(b_file,delimiter=',')\n",
    "    csv_header = next(csvreader)\n",
    "    \n",
    "    months = []\n",
    "    total_revenue = 0\n",
    "    increase_month = 0\n",
    "    decrease_month = 0\n",
    "    \n",
    "    for row in csvreader:\n",
    "        months.append(row[0])\n",
    "        total_revenue += int(row[1])\n",
    "        \n",
    "        if (increase_month<int(row[1])):\n",
    "            increase_month = int(row[1])\n",
    "            inc_actual_month = row[0]\n",
    "            \n",
    "        if (decrease_month>int(row[1])):\n",
    "            decrease_month = int(row[1])\n",
    "            dec_actual_month = row[0]\n",
    "            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Financial Analysis\n",
      "-----------------------------\n",
      "Total Month: 86\n",
      "Total Revenue: $38382578\n",
      "Average Change: $446309.05\n",
      "Greatest Increase in Profits: Feb-12 (1170593)\n",
      "Greatest Decrease in Profits: Sep-13 (-1196225)\n"
     ]
    }
   ],
   "source": [
    "print(\"\\nFinancial Analysis\\n-----------------------------\")\n",
    "print(f\"Total Month: {len(months)}\")\n",
    "print(f\"Total Revenue: ${total_revenue}\")\n",
    "print(f\"Average Change: ${round(total_revenue/len(months),2)}\")\n",
    "print(f\"Greatest Increase in Profits: {inc_actual_month} ({increase_month})\")\n",
    "print(f\"Greatest Decrease in Profits: {dec_actual_month} ({decrease_month})\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
