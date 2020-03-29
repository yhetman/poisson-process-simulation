/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   __mean.c                                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: yhetman <yhetman@student.unit.ua>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2020/03/29 18:19:35 by yhetman           #+#    #+#             */
/*   Updated: 2020/03/29 18:20:48 by yhetman          ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
#include <time.h>

#include "poisson_simulation.h"

double __mean(int n, int vec[] )
{
	int		i;
	double	mean;

	mean = 0.0;
	for (i = 0; i < n; i++)
		mean += (double) vec[i];
	mean /= (double) n;
	return (mean);
}

