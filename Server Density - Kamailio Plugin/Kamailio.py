# Kamailio.py
# Copyright (C) 2014 Sam D Ware <sam.ware@veranetworks.com>
# 
# Kamailio Plugin for Server Density is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# Kamailio Plugin for Server Density is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License along
# with this program.  If not, see <http://www.gnu.org/licenses/>.
# 

import subprocess

class Kamailio (object):
    def __init__(self, agentConfig, checksLogger, rawConfig):
        self.agentConfig = agentConfig
        self.checksLogger = checksLogger
        self.rawConfig = rawConfig
    
    def run(self):
        #define the data dictionary
        data = {'Free Shared Memory (MB)':0,'Total Shared Memory (MB)':0,'Used Shared Memory (MB)':0,'Real Used Shared Memory (MB)':0,'Max Used Shared Memory (MB)':0,'In Use Transactions':0,'Active Transactions':0 }

        # Collecting Free Shared Memory Value
        command = 'sudo /usr/local/sbin/kamctl stats | /bin/grep \'shmem:free_size\' | /bin/sed \'s/shmem:free_size = //\''
        proc = subprocess.Popen(command,shell=True,stdout=subprocess.PIPE)
        output = proc.communicate()[0]
        outnum = 0
        outnum = int(str(output)) / (1024 * 1024)
        data['Free Shared Memory (MB)'] = outnum

        # Collecting Total Shared Memory Value
        c2 = 'sudo /usr/local/sbin/kamctl stats | /bin/grep \'shmem:total_size\' | /bin/sed \'s/shmem:total_size = //\''
        p2 = subprocess.Popen(c2,shell=True,stdout=subprocess.PIPE)
        op2 = p2.communicate()[0]
        on2 = 0
        on2 = int(str(op2)) / (1024 * 1024)
        data['Total Shared Memory (MB)'] = on2

        # Collecting Used Shared Memory Value
        c3 = 'sudo /usr/local/sbin/kamctl stats | /bin/grep \'shmem:used_size\' | /bin/sed \'s/shmem:used_size = //\''
        p3 = subprocess.Popen(c3,shell=True,stdout=subprocess.PIPE)
        op3 = p3.communicate()[0]
        on3 = 0
        on3 = int(str(op3)) / (1024 * 1024)
        data['Used Shared Memory (MB)'] = on3

        # Collecting Real Used Shared Memory Value
        c4 = 'sudo /usr/local/sbin/kamctl stats | /bin/grep \'shmem:real_used_size\' | /bin/sed \'s/shmem:real_used_size = //\''
        p4 = subprocess.Popen(c4,shell=True,stdout=subprocess.PIPE)
        op4 = p4.communicate()[0]
        on4 = 0
        on4 = int(str(op4)) / (1024 * 1024)
        data['Real Used Shared Memory (MB)'] = on4
        
        # Collecting Max Used Shared Memory Value
        c5 = 'sudo /usr/local/sbin/kamctl stats | /bin/grep \'shmem:max_used_size\' | /bin/sed \'s/shmem:max_used_size = //\''
        p5 = subprocess.Popen(c5,shell=True,stdout=subprocess.PIPE)
        op5 = p5.communicate()[0]
        on5 = 0
        on5 = int(str(op5)) / (1024 * 1024)
        data['Max Used Shared Memory (MB)'] = on5

        # Collecting In Use Transactions
        c6 = 'sudo /usr/local/sbin/kamcmd tm.stats | /bin/grep current |  /bin/sed \'s/\W//\' | /bin/sed \'s/current: //\''
        p6 = subprocess.Popen(c6,shell=True,stdout=subprocess.PIPE)
        op6 = p6.communicate()[0]
        on6 = int(str(op6))
        data['In Use Transactions'] = on6

        # Collecting Active Transactions
        c7 = 'sudo /usr/local/sbin/kamctl stats| /bin/grep tmx:active_transactions| /bin/sed \'s/tmx:active_transactions = //\''
        p7 = subprocess.Popen(c7,shell=True,stdout=subprocess.PIPE)
        op7 = p7.communicate()[0]
        on7 = int(str(op7))
        data['Active Transactions'] = on7


        #Return the data dictionary to Server Density
        return data	
