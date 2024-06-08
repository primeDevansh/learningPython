{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "576bde8b-3ca7-4be7-9fa6-e52ce4d79f8e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "-f /Users/devanshrastogi/Library/Jupyter/runtime/kernel-ad163754-7abf-4dac-b7cf-b1a25baeb576.json\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "True"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import webbrowser as wb, sys, pyperclip\n",
    "\n",
    "if len(sys.argv) > 1:\n",
    "    address = ' '.join(sys.argv[1:])\n",
    "else:\n",
    "    address = pyperclip.paste()\n",
    "\n",
    "print(address)\n",
    "wb.open('https://www.google.com/maps/place/' + address)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0c2ebf70-f132-4c69-beec-bf914d772304",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5eede8c6-7f75-4115-98d3-2f7b10f533fc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
