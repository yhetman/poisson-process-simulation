/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   tools.c                                            :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yhetman <yhetman@student.unit.ua>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/29 17:48:42 by yhetman           #+#    #+#             */
/*   Updated: 2020/04/05 20:44:50 by yhetman          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#include "poisson_simulation.h"
# define	DATE_SIZE	40

void	timestamp(void)
{
	static char		date_buff[DATE_SIZE];
	const struct tm	*tm;
	time_t			now;

	now = time();
	tm = localtime(&now);
	strftime(date_buff, DATE_SIZE, "%d %B %Y %I:%M:%S %p", tm);
	fprintf(stdout, "%s\n", date_buff);
}

int		imax_element(int n, int vec[])
{
	int		i;
	int 	value;

	if (n <= 0)
		return (0);
	value = vec[0];
	for (i = 1; i < n; i++)
		if (value < vec[i])
			value = vec[i];
	return (value);
}

int		imin_element(int n, int vec[])
{
	int 	i;
	int 	value;

	if (n <= 0 )
		return (0);
	value = vec[0];
	for (i = 1; i < n; i++)
		if (vec[i] < value)
			value = vec[i];
    return (value);
}


void	output_vec(int n, int vec[], char *str)
{
	int		i;

	fprintf(stdout, "\n");
	fprintf(stdout, "%s\n", str);
	fprintf(stdout, "\n");
	for (i = 0; i < n; i++ )
		fprintf(stdout, "  %6d: %8d\n", i, vec[i]);
}

# undef		DATE_SIZE
