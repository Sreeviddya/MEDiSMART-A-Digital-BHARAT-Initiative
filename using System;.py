using System; 
using System.Collections.Generic; 

class Process 
{ 
public int pid; // Process ID 
	public int bt; // CPU Burst time required 
	public int priority; // Priority of this process 
public Process(int pid, int bt, int priority) 
{ 
	this.pid = pid; 
	this.bt = bt; 
	this.priority = priority; 
} 

public int Prior 
{ 
	get { return priority; } 
} 
} 

class GFG 
{ 
// Function to find the waiting time for all processes 
public void findWaitingTime(Process[] proc, int n, int[] wt) 
{ 
// waiting time for first process is 0 
wt[0] = 0; 
	// calculating waiting time 
	for (int i = 1; i < n; i++) 
		wt[i] = proc[i - 1].bt + wt[i - 1]; 
} 

// Function to calculate turn around time 
public void findTurnAroundTime(Process[] proc, int n, int[] wt, int[] tat) 
{ 
	// calculating turnaround time by adding 
	// bt[i] + wt[i] 
	for (int i = 0; i < n; i++) 
		tat[i] = proc[i].bt + wt[i]; 
} 

// Function to calculate average time 
public void findavgTime(Process[] proc, int n) 
{ 
	int[] wt = new int[n]; 
	int[] tat = new int[n]; 
	int total_wt = 0; 
	int total_tat = 0; 

	// Function to find waiting time of all processes 
	findWaitingTime(proc, n, wt); 

	// Function to find turn around time for all processes 
	findTurnAroundTime(proc, n, wt, tat); 

	// Display processes along with all details 
	Console.WriteLine("\nProcesses Burst time Waiting time Turn around time"); 

	// Calculate total waiting time and total turn around time 
	for (int i = 0; i < n; i++) 
	{ 
		total_wt = total_wt + wt[i]; 
		total_tat = total_tat + tat[i]; 
		Console.WriteLine(" " + proc[i].pid + "\t\t" + proc[i].bt + "\t " + wt[i] + "\t\t " + tat[i]); 
	} 

	Console.WriteLine("\nAverage waiting time = " + (float)total_wt / (float)n); 
	Console.WriteLine("Average turn around time = " + (float)total_tat / (float)n); 
} 

public void priorityScheduling(Process[] proc, int n) 
{ 
	// Sort processes by priority 
	Array.Sort(proc, new Comparison<Process>((a, b) => b.Prior.CompareTo(a.Prior))); 
	Console.WriteLine("Order in which processes gets executed "); 

	for (int i = 0; i < n; i++) 
		Console.Write(proc[i].pid + " "); 

	findavgTime(proc, n); 
} 

// Driver code 
static void Main(string[] args) 
{ 
	GFG ob = new GFG(); 
	int n = 3; 
	Process[] proc = new Process[n]; 
	proc[0] = new Process(1, 10, 2); 
	proc[1] = new Process(2, 5, 0); 
	proc[2] = new Process(3, 8, 1); 
	ob.priorityScheduling(proc, n); 
} 
} 
