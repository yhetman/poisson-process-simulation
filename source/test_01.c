/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   main.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yhetman <yhetman@student.unit.ua>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/29 13:35:02 by yhetman           #+#    #+#             */
/*   Updated: 2020/04/03 15:52:39 by yhetman          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <string.h>

#include "poisson_simulation.h"

int		main ( )
{
	timestamp();
	printf("\n");
	printf("POISSON_SIMULATION_TEST\n");
    test01();
	printf("\n");
	printf("POISSON_SIMULATION_TEST\n");
	printf("  Normal end of execution.\n\n");
	timestamp();
	return 0;
}

void	welcome_print(double lambda, int events)
{
	printf ( "\n" );
	printf ( "TEST01:\n" );
	printf ( "  POISSON_FIXED_EVENTS simulates a Poisson process\n" );
	printf ( "  until a given number of events have occurred.\n" );
	printf ( "\n" );
	printf ( "  Simulate a Poisson process, for which, on average,\n" );
	printf ( "  LAMBDA events occur per unit time.\n" );
	printf ( "  Run until you have observed EVENT_NUM events.\n" );
	printf ( "\n" );
	printf ( "  LAMBDA = %g\n", lambda );
	printf ( "  EVENT_NUM = %d\n", events);
}

void	wait_time_print(int	event_num, double *w)
{
	double	min;
	double	max;
	double	ave;

	min = r8vec_min ( event_num + 1, w );
	max = r8vec_max ( event_num + 1, w );
	ave = r8vec_mean ( event_num + 1, w );
	printf ( "\n" );
	printf ( "  Minimum wait = %g\n", min );
	printf ( "  Average wait = %g\n", ave );
	printf ( "  Maximum wait = %g\n", max );
    printf ( "\n" );
	printf ( " Count            Time            Wait\n" );
	printf ( "\n" );
}

void	create_file(char *file_name)
{
	FILE	*command;

	
	command = fopen ( file_name, "wt" );
	fprintf ( command, "# poisson_timeline_commands.txt\n" );
	fprintf ( command, "#\n" );
	fprintf ( command, "# Usage:\n" );
	fprintf ( command, "#  gnuplot < poisson_timeline_commands.txt\n" );
	fprintf ( command, "#\n" );
	fprintf ( command, "set term png\n" );
	fprintf ( command, "set output 'poisson_timeline.png'\n" );
	fprintf ( command, "set style data lines\n" );
	fprintf ( command, "set xlabel 'Time'\n" );
	fprintf ( command, "set ylabel 'Number of Events'\n" );
	fprintf ( command, "set title 'Observation of Fixed Number of Poisson Events'\n" );
	fprintf ( command, "set grid\n" );
	fprintf ( command, "plot 'poisson_timeline_data.txt' using 1:2 lw 2\n" );
	fprintf ( command, "quit\n" );
    fclose ( command );
	printf ( "  Plot commands stored in \"%s\".\n", file_name );
}

void	create_time_file(char file_name, double width)
{
	FILE	*command;

	command = fopen ( command_filename, "wt" );
	fprintf ( command, "# poisson_times_commands.txt\n" );
	fprintf ( command, "#\n" );
	fprintf ( command, "# Usage:\n" );
	fprintf ( command, "#  gnuplot < poisson_times_commands.txt\n" );
	fprintf ( command, "#\n" );
	fprintf ( command, "set term png\n" );
	fprintf ( command, "set output 'poisson_times.png'\n" );
	fprintf ( command, "set xlabel 'Waiting Time'\n" );
	fprintf ( command, "set ylabel 'Frequency'\n" );
	fprintf ( command, "set title 'Waiting Times Observed Over Fixed Time'\n" );
	fprintf ( command, "set grid\n" );
	fprintf ( command, "set style fill solid\n" );
	fprintf ( command, "plot 'poisson_times_data.txt' using 1:2:(%g) with boxes\n", width );
	fprintf ( command, "quit\n" );
	fclose ( command );
	printf ( "  Plot commands stored in \"%s\".\n", file_name );
}

void test01()
{
	int bin_num = 30;
	char command_filename[80];
	char data_filename[80];
	FILE *data;
	int event_num = 1000;
	int *f_bin;
	int i;
	int j;
	double lambda = 0.5;
	int seed = 31415926;
	double *t;
	double *w;
	double *w_bin;
	double	w_min;
	double	w_max;
	double width;

	welcome_print(double lambda, int event_num);
	t = ( double * ) malloc ( ( event_num + 1 ) * sizeof ( double ) );
	w = ( double * ) malloc ( ( event_num + 1 ) * sizeof ( double ) );
	poisson_fixed_events ( lambda, event_num, &seed, t, w );
	wait_time_print(event_num, w);
	for ( i = 0; i <= 5; i++ )
		printf ( "  %d  %g  %g\n", i, t[i], w[i] );
	printf ( "  ....  ..............  ..............\n" );
	for ( i = event_num - 5; i <= event_num; i++ )
	    printf ( "  %d  %g  %g\n", i, t[i], w[i] );
	strcpy(data_filename, "poisson_timeline_data.txt" );
	data = fopen ( data_filename, "wt" );
	for ( i = 0; i <= event_num; i++ )
		fprintf(data, "  %g  %d\n", t[i], i );
	fclose (data );
	printf (" \n" );
	printf ("  Data stored in \"%s\".\n", data_filename );
	strcpy (command_filename, "poisson_timeline_commands.txt" );
	create_file(command_filename);
	printf ("  Plot commands stored in \"%s\".\n", command_filename );
	w_min = r8vec_min (event_num + 1, w );
	w_max = r8vec_max (event_num + 1, w );
	w_bin = r8vec_midspace_new (bin_num, w_min, w_max );
	f_bin = ( int * ) malloc (bin_num * sizeof ( int ) );
    for ( i = 0; i < bin_num; i++ )
		f_bin[i] = 0;
	for ( i = 0; i <= event_num; i++ )
	{
		j = 1 + ( int ) ( ( double ) (bin_num ) * ( w[i] - w_min ) / ( w_max - w_min ) );
		j = MIN ( j, bin_num );
		f_bin[j] = f_bin[j] + 1;
	}
	strcpy (data_filename, "poisson_times_data.txt" );
	data = fopen (data_filename, "wt" );
	for ( i = 0; i < bin_num; i++ )
		fprintf (data, "  %g  %d\n", w_bin[i], f_bin[i] );}
	fclose (data);
	printf ( " \n" );
	printf ( "  Data ssstored in \"%s\".\n", data_filename );
	strcpy ( command_filename, "poisson_times_commands.txt" );
	width = 0.85 * ( w_max - w_min ) / ( double ) ( bin_num );
	create_time_file(command_filename, width);
	free ( f_bin );
	free ( t );
	free ( w );
	free ( w_bin );
}
