{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "csvpath = os.path.join(\"..\",\"Resources\",\"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "total_votes = 0\n",
    "candidates = []\n",
    "vcount = []\n",
    "winnervcount = 0\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(csvpath, 'r', newline='') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=',')\n",
    "    csv_header = next(csvreader)\n",
    "    \n",
    "    for row in csvreader: \n",
    "        total_votes+=1\n",
    "        \n",
    "        if (row[2] not in candidates):\n",
    "            candidates.append(row[2])\n",
    "            vcount.append(0)\n",
    "            \n",
    "        candidateindex = candidates.index(row[2])\n",
    "        vcount[candidateindex] += 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Election Results\n",
      "------------------------------\n",
      "Total Votes: 3521001\n",
      "-------------------------\n",
      "Khan: 63.0% (2218231)\n",
      "Correy: 20.0% (704200)\n",
      "Li: 14.0% (492940)\n",
      "O'Tooley: 3.0% (105630)\n",
      "------------------------\n",
      "Winner: Khan\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "print(f\"\\nElection Results\\n------------------------------\")\n",
    "print(f\"Total Votes: {total_votes}\")\n",
    "print(\"-------------------------\")\n",
    "\n",
    "for r in range(len(candidates)):\n",
    "    votepercentage = round((vcount[r]/total_votes)*100,2)\n",
    "    print(f\"{candidates[r]}: {votepercentage}% ({vcount[r]})\")\n",
    "    if (winnervcount<vcount[r]):\n",
    "        winnervcount = vcount[r]\n",
    "        winner = candidates[r]\n",
    "        \n",
    "print(\"------------------------\")\n",
    "print(f\"Winner: {winner}\\n-------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
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
