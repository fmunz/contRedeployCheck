#
# after setting the environment (e.g. by running setDomainEnv.sh) run this script as
# java weblogic.WLST deployLoop.py
# or 
# java weblogic.WLST deployLoop.py > output.txt

dep= '/u01/Oracle/Middleware12.1.1/wlserver_12.1/samples/server/medrec/modules/medrec/assembly/target/medrec.ear'
t='MedRecServer'

connect('weblogic','welcome1','t3://localhost:7011')
System.out.println("connected")
custom()

for x in range(1000):
	i=str(x)
	System.out.println("\n\t### redeployment iteration number: " + i);
	deploy('medrec',dep,targets=t,block="true")
	java.lang.Thread.sleep(30*1000)	
	undeploy( 'medrec',block="true")
	java.lang.Thread.sleep(30*1000)	
	
	# comment/remove the lines below if you don't like any output
	#
	# output classes loaded	
	cd('/java.lang/java.lang:type=ClassLoading')
	cloaded=str(get('LoadedClassCount'))
	System.out.println("\n\t loaded classes:"+cloaded)

	# output non-heap details
	cd('/java.lang/java.lang:type=Memory')
	n = str(get('NonHeapMemoryUsage'))
	System.out.println("\n\t non heap usage:"+n)

	# output heap details
	cd('/java.lang/java.lang:type=Memory')
	h = str(get('HeapMemoryUsage'))
	System.out.println("\n\t non heap usage:"+h)

