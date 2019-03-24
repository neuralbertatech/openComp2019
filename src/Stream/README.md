Need to integrate the different Window states with streams

Acquire_Stream.py - Initializes the LSL stream, ensuring that we are prepared to record acquire data
Acquire_Data.py will be ran in the background constantly immediately after Acquire_Stream.py connects

After the initial 5 seconds of appropriate data collection for a baseline, the following one second trials will begin and continue until the shift away from game_state:

On a given trial:
1. 1 second timer start & Feature extraction from Current_Epoch into Current_Cache (there will be three types of analysis to play with)

2. An evaluation of features in comparison to Last_Cache a structure of x past epochs, and an appropriate change in game_state characteristics

3. The front bumper of the buffer updates (Incoming_Epoch becomes Imed_Epoch) and evaluates (Imed_Epoch (1 second)) via buffer_tools.preprocessing() if at a quick pass this is determined to not contain signifigant artifacts then continue to number 3
      if however - there are significant artifacts, update will wait for another second (skip all remaining trial steps) - until an appropriate Imed_Epoch is acquired.

4. If there are no significant artifacts:
      then all EEG data structures cascade from the bottom up:
Current_Cache is added to the Last_Cache, overwriting the oldest event Last_Cache
Current_Epoch
Imed_Epoch becomes Current_Epoch
Incoming_Epoch becomes Imed_Epoch

the next trial is ready to begin once a 1 second timer is up



Stream
|----Acquire_Stream.py                    # Establish LSL stream
|----Acquire_Data.py                      # Take from LSL stream
|----Initialize_Buffer.py                 # Create empty buffer structures
|----Eden_Buffer_Master.py                # wrapper
|----Eden_Buffer_Action_Tools.py          # my way of doing things
|    |----buffer_tools
|         |----preprocessing()            # ignore update?
|         |----analysis_type()            
|         |    |----temporal_analysis()
|         |    |----band_analysis()
|         |    |----wavelet_analysis()
|         |----evaluate()                 # what change to game state?
|         |----update(epoch)              # shift down from bottom to top
|----Buffer_file                          # premade function I am cutting down from


  add trial_state back into Eden_Buffer_Action_Tools

Get familiar with:
get_last_data
compute_feature_vector (likely too complicated, simplify)
update_buffer
pull_chunk
