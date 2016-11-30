__author__ = 'Callum'

int = 1
mstart = 0
clength = 1
cstart = 0
array = [1,2,3,4,5,1,2,4,5]

def subSequence(int,mstart,clength,cstart,array):
    for int < len(array)(int,mstart,clength,cstart,array):

        if array[i] > array[i-1](array(int,mstart,clength,cstart,array):
            clength+1

            if clength > mlen:
                mlen = clength
                mstart = cstart
            else:
                clength = 1
                cstart = i



"""def Sequence(integers):

  longest_sequence = []
  current_sequence = []

  for i in range( len(integers) ):

    if i < len(integers) - 1 and integers[i] <= integers[i+1]:   # sequence continues
      current_sequence.append(integers[i])
      print('current_sequence ', current_sequence)

    else:                           # else sequence, or input, ends now
      current_sequence.append(integers[i])   # catch this last number in sequence, too
      print('\nsubseq ended ', current_sequence)

      # now we've hit the end of a subsequence
      # do we replace the stored one, or not?
      if len(current_sequence) > len(longest_sequence):
        print('\nreplacing previous longest ', longest_sequence)

        longest_sequence = current_sequence

      # either way, reset the current sequence tracker
      current_sequence = []

  print()
  print ('Finished. Longest found: ', longest_sequence)


Sequence([1,2,3,4,5,1,2,4,5])
print('\n----\n')
Sequence([1,2,4,5,1,2,3,4,5])"""